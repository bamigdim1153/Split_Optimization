from pathlib import Path
import sys,json,ast,contextlib,io,os,time,traceback,base64
ROOT=Path(__file__).resolve().parents[1]
def execute(path,output):
 import matplotlib;matplotlib.use('Agg')
 import matplotlib.pyplot as plt
 path=Path(path).resolve();output=Path(output).resolve();output.mkdir(parents=True,exist_ok=True)
 nb=json.loads(path.read_text(encoding='utf-8'));ns={'__name__':'__course_notebook__'};count=0;old=Path.cwd();os.chdir(output)
 try:
  for cell in nb['cells']:
   if cell['cell_type']!='code':continue
   count+=1;stream=io.StringIO();outputs=[];cell['execution_count']=count
   def show(*args,**kwargs):
    for number in plt.get_fignums():
     fig=plt.figure(number);data=io.BytesIO();fig.savefig(data,format='png',dpi=120,bbox_inches='tight')
     outputs.append({'output_type':'display_data','metadata':{},'data':{'image/png':base64.b64encode(data.getvalue()).decode(),'text/plain':['Matplotlib figure']}})
    plt.close('all')
   plt.show=show
   start=time.time()
   print('Executing',path.name,'cell',count,flush=True)
   try:
    with contextlib.redirect_stdout(stream),contextlib.redirect_stderr(stream):
     tree=ast.parse(''.join(cell['source']))
     last=tree.body[-1] if tree.body else None
     if isinstance(last,ast.Expr) and not isinstance(last.value,ast.Call):
      tree.body=tree.body[:-1];exec(compile(tree,str(path),'exec'),ns)
      value=eval(compile(ast.Expression(last.value),str(path),'eval'),ns)
      if value is not None:
       text=value.to_string(index=False) if hasattr(value,'to_string') else repr(value)
       outputs.append({'output_type':'execute_result','execution_count':count,'metadata':{},'data':{'text/plain':[text]}})
     else:exec(compile(tree,str(path),'exec'),ns)
    if stream.getvalue():outputs.insert(0,{'output_type':'stream','name':'stdout','text':stream.getvalue().splitlines(True)})
    cell['outputs']=outputs;cell['metadata']['execution_seconds']=round(time.time()-start,4)
   except Exception as e:
    cell['outputs']=[{'output_type':'error','ename':type(e).__name__,'evalue':str(e),'traceback':traceback.format_exc().splitlines()}]
    path.write_text(json.dumps(nb,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');raise
  path.write_text(json.dumps(nb,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 finally:os.chdir(old)
 print('COMPLETED',path.name,count,flush=True)
if __name__=='__main__':
 execute(sys.argv[1],sys.argv[2])
