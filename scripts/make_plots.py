import matplotlib.pyplot
import pandas
import argparse


def enquote(text, use_tex):
    if use_tex:
        return f"``{text}''"
    else:
        return f'"{text}"'


LABEL_DICT = {
    "WORK": "Workload",
    "LEVL": "Level",
    "ASS1": "Assignment 1",
    "ASS2": "Assignment 2",
    "ASS3": "Assignment 3",
    "ASS4": "Assignment 4",
    "ILAL": "I learned a lot from the course",
    "INTC": "The course was intellectually challenging",
    "CSTR": "The course was clearly structured",
    "FACT": "Factual knowledge",
    "FUND": "Fundamental principles",
    "CURR": "Current theories",
    "APPL": "To apply subject matter",
    "PROF": "Professional skills",
    "TECH": "Technical skills",
}

PLOT_WIDTH = 3.333
PLOT_HEIGHT = 1.25
FIVE_POINT_LIMIT = (0.8, 5.2)
YEARS_LIMIT = (2016.9, 2023.1)
YEAR_TICKS = [2017, 2018, 2019, 2020, 2021, 2022, 2023]
AGREE_DISAGREE_SCALE = [
    "Firmly Disagree",
    "Disagree",
    "Neutral",
    "Agree",
    "Firmly Agree",
]
RIGHTNESS_SCALE = ["Too Low", "Low", "Just Right", "High", "Too High"]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--tex", action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args()

    matplotlib.rcParams.update(
        {
            "figure.labelsize": "medium",
            "figure.titlesize": "medium",
            "axes.labelsize": "medium",
            "axes.titlesize": "medium",
            "legend.fontsize": "small",
            "legend.handlelength": 1.0,
            "legend.handletextpad": 0.4,
            "legend.borderaxespad": 0.25,
            "legend.labelspacing": 0.25,
            "legend.columnspacing": 0.75,
            "font.size": 8 if args.tex else 6,
            "legend.loc": "lower left",
            "font.family": "serif",
            "text.usetex": args.tex,
            "text.latex.preamble": """
            \\usepackage{libertine}
            \\usepackage[libertine]{newtxmath}
            """,
            "figure.constrained_layout.use": True,
            "savefig.bbox": "tight",
            "savefig.pad_inches": 0.01,
        }
    )

    students_df = pandas.read_csv("../data/students.csv")

    # Make the student count plot
    fig, axs = matplotlib.pyplot.subplots(
        figsize=(PLOT_WIDTH, PLOT_HEIGHT),
        nrows=1,
        ncols=1,
    )

    axs.set_xlabel("Year")
    axs.set_ylabel("Students")

    total_df = students_df[["year", "n_students"]].dropna()
    resp_df = students_df[["year", "n_resp"]].dropna()

    axs.plot(
        total_df["year"],
        total_df["n_students"],
        marker="x",
        markersize=3.5,
        linewidth=1,
        label="Total enrolled",
    )
    axs.plot(
        resp_df["year"],
        resp_df["n_resp"].dropna(),
        marker="x",
        markersize=3.5,
        linewidth=1,
        label="Evaluation respondents",
    )

    axs.set_ylim(bottom=0)
    axs.set_xlim(YEARS_LIMIT)
    axs.grid(axis="both")
    axs.legend()
    fig.savefig("n_students.pdf")

    metrics_df = pandas.read_csv("../data/metrics.csv").dropna()
    metrics_df["count"] = (
        metrics_df["n1"]
        + metrics_df["n2"]
        + metrics_df["n3"]
        + metrics_df["n4"]
        + metrics_df["n5"]
    )
    metrics_df["mean"] = (
        1 * metrics_df["n1"]
        + 2 * metrics_df["n2"]
        + 3 * metrics_df["n3"]
        + 4 * metrics_df["n4"]
        + 5 * metrics_df["n5"]
    ) / metrics_df["count"]

    # Make the feedback plot
    fig, [ax1, ax2, ax3, ax4] = matplotlib.pyplot.subplots(
        figsize=(PLOT_WIDTH, 5), nrows=4, ncols=1, sharex=True
    )

    # Make the general outcomes plot
    ax1.set_title("General statements about the course")
    ax1.set_yticks(
        [1, 2, 3, 4, 5],
        labels=AGREE_DISAGREE_SCALE,
    )

    for metric in ["ILAL", "CSTR", "INTC"]:
        tmp_df = metrics_df[metrics_df["metric"] == metric]
        ax1.plot(
            tmp_df["year"],
            tmp_df["mean"],
            label=enquote(LABEL_DICT.get(metric, metric), args.tex),
            marker="x",
            markersize=3.5,
            linewidth=1,
        )

    ax1.set_ylim(FIVE_POINT_LIMIT)
    ax1.set_xlim(YEARS_LIMIT)
    ax1.legend()
    ax1.grid(axis="both")

    # Make the learning outcomes plot
    if args.tex:
        ax2.set_title("``I acquired, learned, or developed \ldots{}''")
    else:
        ax2.set_title('"I acquired, learned, or developed ..."')
    ax2.set_yticks(
        [1, 2, 3, 4, 5],
        labels=AGREE_DISAGREE_SCALE,
    )

    for metric in ["FACT", "FUND", "CURR", "APPL", "PROF", "TECH"]:
        tmp_df = metrics_df[metrics_df["metric"] == metric]
        ax2.plot(
            tmp_df["year"],
            tmp_df["mean"],
            label=LABEL_DICT.get(metric, metric),
            marker="x",
            markersize=3.5,
            linewidth=1,
        )

    ax2.legend(ncols=2)
    ax2.grid(axis="both")
    ax2.set_ylim(FIVE_POINT_LIMIT)
    ax2.set_xlim(YEARS_LIMIT)

    # Make the assignments plot
    if args.tex:
        ax3.set_title("``\ldots{} helped me understand the subject matter''")
    else:
        ax3.set_title('"... helped me understand the subject matter"')
    ax3.set_yticks(
        [1, 2, 3, 4, 5],
        labels=AGREE_DISAGREE_SCALE,
    )

    for metric in ["ASS1", "ASS2", "ASS3", "ASS4"]:
        tmp_df = metrics_df[metrics_df["metric"] == metric]
        ax3.plot(
            tmp_df["year"],
            tmp_df["mean"],
            label=LABEL_DICT.get(metric, metric),
            marker="x",
            markersize=3.5,
            linewidth=1,
        )

    ax3.set_ylim(FIVE_POINT_LIMIT)
    ax3.set_xlim(YEARS_LIMIT)
    ax3.grid(axis="both")
    ax3.legend(ncols=2)

    # Make the workloads plot
    if args.tex:
        ax4.set_title("``The \ldots{} of the course was \ldots{}''")
    else:
        ax4.set_title('"The ... of the course was ..."')
    ax4.set_xlabel("Year")
    ax4.set_yticks([1, 2, 3, 4, 5], labels=RIGHTNESS_SCALE)
    ax4.set_xticks(YEAR_TICKS)

    for metric in ["WORK", "LEVL"]:
        tmp_df = metrics_df[metrics_df["metric"] == metric]
        ax4.plot(
            tmp_df["year"],
            tmp_df["mean"],
            label=LABEL_DICT.get(metric, metric),
            marker="x",
            markersize=3.5,
            linewidth=1,
        )

    ax4.set_ylim(FIVE_POINT_LIMIT)
    ax4.set_xlim(YEARS_LIMIT)
    ax4.grid(axis="both")
    ax4.legend()

    fig.savefig("feedback.pdf")
