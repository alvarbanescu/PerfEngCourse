import pandas

from common import *

PLOT_WIDTH = 3.333
PLOT_HEIGHT = 1.25
FIVE_POINT_LIMIT = (0.8, 5.2)
YEARS_LIMIT = (2016.9, 2023.1)
YEAR_TICKS = [2017, 2018, 2019, 2020, 2021, 2022, 2023]


RANKING_CLUSTERS = [
    (
        "\\enquote{The course \ldots{}}",
        [
            "ILAL",
            "CSTR",
            "INTC",
        ],
    ),
    (
        "\\enquote{I acquired, learned, or developed \ldots{}}",
        [
            "FACT",
            "FUND",
            "CURR",
            "APPL",
            "PROF",
            "TECH",
        ],
    ),
    (
        "\\enquote{\ldots{} helped me understand the subject}",
        [
            "ASS1",
            "ASS2",
            "ASS3",
            "ASS4",
        ],
    ),
]

RIGHTNESS_CLUSTERS = [
    (
        "\\enquote{The \ldots{} of the course was}",
        [
            "WORK",
            "LEVL",
        ],
    ),
]


def write_header(f, s):
    f.write(
        "\\begin{tabular}{p{1mm} p{4.2cm} R{3mm} R{3mm} R{3mm} R{3mm} R{3mm} R{4mm}}"
    )
    f.write("\\toprule")
    f.write(
        "\\multicolumn{2}{l}{Statement} & %s & $M$ \\\\\\midrule"
        % (
            " & ".join(
                "\\multicolumn{1}{r}{\\rotatebox[origin=l]{90}{\\smash{%s}}}"
                % q
                for q in s
            )
        )
    )


def write_body(f, c):
    for n, v in c:
        f.write("\\multicolumn{2}{l}{%s} \\\\" % (n))

        for i in v:
            rel = df.loc[[i]]
            N = (
                rel["n1"].sum()
                + rel["n2"].sum()
                + rel["n3"].sum()
                + rel["n4"].sum()
                + rel["n5"].sum()
            )
            W = (
                rel["n1"].sum()
                + 2 * rel["n2"].sum()
                + 3 * rel["n3"].sum()
                + 4 * rel["n4"].sum()
                + 5 * rel["n5"].sum()
            )
            f.write(
                "& %s & %d & %d & %d & %d & %d & %3.1f \\\\"
                % (
                    LABEL_DICT[i],
                    rel["n1"].sum(),
                    rel["n2"].sum(),
                    rel["n3"].sum(),
                    rel["n4"].sum(),
                    rel["n5"].sum(),
                    W / N,
                )
            )


def write_footer(f):
    f.write("\\bottomrule")
    f.write("\\end{tabular}")


if __name__ == "__main__":
    metrics_df = pandas.read_csv(
        "../data/metrics.csv",
        dtype={
            "n1": "Int64",
            "n2": "Int64",
            "n3": "Int64",
            "n4": "Int64",
            "n5": "Int64",
        },
    )

    df = metrics_df.groupby(["metric"]).sum()

    with open("eval_agree_disagree.tex", "w") as f:
        write_header(f, AGREE_DISAGREE_SCALE)
        write_body(f, RANKING_CLUSTERS)
        write_footer(f)

    with open("eval_low_high.tex", "w") as f:
        write_header(f, RIGHTNESS_SCALE)
        write_body(f, RIGHTNESS_CLUSTERS)
        write_footer(f)
