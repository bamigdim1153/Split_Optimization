library(PRISMA2020)
input <- read.csv("session_04/prisma_official_input.csv", stringsAsFactors=FALSE)
data <- PRISMA_data(input)
# Report-level synthesis; do not invent an independent-study count.
data$new_studies <- "unresolved"
data$total_studies <- "unresolved"
plot <- PRISMA_flowdiagram(data, previous=FALSE, other=TRUE,
                           interactive=FALSE, fontsize=11,
                           title_colour="LightBlue", greybox_colour="Gainsboro")
out <- "session_04/prisma_official"
dir.create(out, recursive=TRUE, showWarnings=FALSE)
PRISMA_save(plot, filename=file.path(out,"flow.svg"), overwrite=TRUE)
PRISMA_save(plot, filename=file.path(out,"flow.png"), overwrite=TRUE, width=2200)
PRISMA_save(plot, filename=file.path(out,"flow.pdf"), overwrite=TRUE)
writeLines(capture.output(sessionInfo()), file.path(out,"R_sessionInfo.txt"))
writeLines(c(paste("PRISMA2020 package:",as.character(packageVersion("PRISMA2020"))),
  "Generated with the PRISMA2020 package linked by the official PRISMA website.",
  "Count input is tracked; no independent-study count has been fabricated."),
  file.path(out,"generation.txt"))
