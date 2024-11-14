import matplotlib.pyplot as plt
import logging
import datetime
import os

# Set up logging for the module
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

class StockPlotter:

    @staticmethod
    def plot_data(df, save_figure=False, figure_filename=None, bar_width=0.6, font_size=12, dpi=700):
        """Plot stock ratings in a bar plot.
        
        Args:
            df (pd.DataFrame): Pandas DataFrame containing stock data. It must have columns ['Symbol', 'Rate'].
            save_figure (bool): Whether to save the plot as an image file. Defaults to False.
            figure_filename (str, optional): Filename to save the plot. If None, a default filename is generated.
            bar_width (float): Width of the bars in the bar plot. Defaults to 0.6.
            font_size (int): Font size for plot labels. Defaults to 12.
            dpi (int): Dots per inch for the saved image. Defaults to 700.
        """
        # Ensure that the DataFrame contains the necessary columns
        if 'Symbol' not in df or 'Rate' not in df:
            logging.error("DataFrame must contain 'Symbol' and 'Rate' columns.")
            return
        
        # Create the bar plot
        plt.bar(df['Symbol'], df['Rate'], color='skyblue', width=bar_width)
        plt.xlabel('Symbol', fontsize=font_size)
        plt.ylabel('Rate', fontsize=font_size)
        plt.title('Stock Ratings', fontsize=font_size)
        plt.xticks(rotation=45, ha='right', fontsize=font_size)
        plt.tight_layout()

        # Save the figure if required
        if save_figure:
            if figure_filename is None:
                current_time = datetime.datetime.now().strftime("%d-%m-%Y")
                figure_filename = os.path.join("results", f"plot_{current_time}.png")
            
            # Ensure that the directory exists
            os.makedirs(os.path.dirname(figure_filename), exist_ok=True)
            
            # Save the figure with the specified DPI
            plt.savefig(figure_filename, dpi=dpi)
            logging.info(f"Figure saved as {figure_filename}.")  # Log that the figure has been saved
        else:
            # Display the plot if not saving it
            plt.show()

