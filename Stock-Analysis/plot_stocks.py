import matplotlib.pyplot as plt
import logging
import datetime

class StockPlotter:

    @staticmethod
    def plot_data(df, save_figure=False, figure_filename="plot.png", bar_width=0.6, font_size=3, dpi=700):
        """Plot stock ratings.
        
        Args:
            df (DataFrame): Pandas DataFrame containing stock data.
            save_figure (bool): Whether to save the plot as an image file.
            figure_filename (str): Filename to save the plot.
            bar_width (float): Width of the bars in the bar plot.
            font_size (int): Font size for plot labels.
            dpi (int): Dots per inch for the saved image.
        """
        plt.bar(df['Symbol'], df['Rate'], color='skyblue', width=bar_width)
        plt.xlabel('Symbol', fontsize=font_size)
        plt.ylabel('Rate', fontsize=font_size)
        plt.title('Stock Ratings', fontsize=font_size)
        plt.xticks(rotation=45, ha='right', fontsize=font_size)
        plt.tight_layout()
        if save_figure:
            current_time = datetime.datetime.now().strftime("%d-%m-%Y")
            figure_filename = f"/workspaces/Python_Project/Stock-Analysis/results/plot_{current_time}.png"
            plt.savefig(figure_filename, dpi=dpi)  # Save the figure to a file with higher resolution
            logging.getLogger(__name__).info(f"Figure saved as {figure_filename}.")  # Log that the figure has been saved
        else:
            plt.show()