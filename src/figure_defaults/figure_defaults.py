import matplotlib as mpl
import matplotlib
import collections

class FigureDefaults:
    def __init__(self, style='default', rc_params=None, **kwargs):
        """ Initializes FigureDefaults object. Changes made to the object are reflected to the mpl.rcParams as side effects.

        Args:
            style (str): style string, can be {default, large, nature_sc, nature_dc, presentation} or a pointer to an initialization function with signature "func(self)".
            rc_params (dict or object): mpl.rcParams will updated with these values. Has to be dict with key-value pairs. Be careful when directly modifying rc_params, the FigureDefaults object cannot follow the changes made this way.
            kwargs: key-value arguments, where keys can be any property.
        """
        self.style = style
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.rc_params = rc_params

    def reset(self):
        """ Resets the rcParams to defaults. """
        mpl.rcParams.update(mpl.rcParamsDefault)

    @property
    def rc_params(self):
        return mpl.rcParams

    @rc_params.setter
    def rc_params(self, value):
        if value is not None:
            mpl.rcParams.update(value)

    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, value):
        """ Setting the style overrides all the other settings. """
        if value is None:
            value = 'default'

        if callable(value):
            value(self)
            self._style = value.__name__
        else:
            self._style = value
            options = {'default': lambda: None,
                       'large': self.large,
                       'nature_sc': self.nature_sc,
                       'nature_dc': self.nature_dc,
                       'anc_style': self.anc_style,
                       'presentation': self.presentation,
                       'pr_single_column': self.pr_single_column,
                       'pr_double_column': self.pr_double_column,
                       'pr_one_and_half_column': self.pr_one_and_half_column,
                       }
            options[self._style]()

    @property
    def fontsize(self):
        if hasattr(self, '_fontsize'):
            return self._fontsize
        else:
            return matplotlib.rcParams['font.size']

    @fontsize.setter
    def fontsize(self, value):
        self._fontsize = value
        matplotlib.rcParams['font.size'] = value

    @property
    def aspect_ratio(self):
        if hasattr(self, '_aspect_ratio'):
            return self._aspect_ratio
        else:
            #return mpl.rcParams['figure.figsize'][0]/mpl.rcParams['figure.figsize'][1]
            return 4/3

    @aspect_ratio.setter
    def aspect_ratio(self, value):
        self._aspect_ratio = value
        self._set_figure_dimensions()

    @property
    def figure_size(self):
        if hasattr(self, '_figure_size'):
            return self._figure_size
        else:
            #return matplotlib.rcParams['figure.figsize'][0]
            return 6.1

    @figure_size.setter
    def figure_size(self, value):
        self._figure_size = value
        self._set_figure_dimensions()

    def _set_figure_dimensions(self):
        matplotlib.rcParams['figure.figsize'] = (self.figure_size*self.size_fraction_x, self.figure_size*self.size_fraction_y/self.aspect_ratio)

    @property
    def font(self):
        if hasattr(self, '_font'):
            return self._font
        else:
            return mpl.rcParams['font.family']

    @font.setter
    def font(self, value):
        self._font = value
        #mpl.rcParams['font.family']
        #mpl.rcParams['font.family'] = 'serif'
        mpl.rcParams['font.sans-serif'] = value
        
    @property
    def axes_linewidth(self):
        if hasattr(self, '_axes_linewidth'):
            return self._axes_linewidth
        else:
            return mpl.rcParams['axes.linewidth']
        
    @axes_linewidth.setter
    def axes_linewidth(self, value):
        mpl.rcParams['axes.linewidth'] = value
        self._axes_linewidth = value

    @property
    def linewidth(self):
        if hasattr(self, '_linewidth'):
            return self._linewidth
        else:
            return mpl.rcParams['lines.linewidth']

    @linewidth.setter
    def linewidth(self, value):
        mpl.rcParams['lines.linewidth'] = value
        self._linewidth = value

    @property
    def linewidth_narrow(self):
        if hasattr(self, '_linewidth_narrow'):
            return self._linewidth_narrow
        else:
            return self.linewidth/2

    @linewidth_narrow.setter
    def linewidth_narrow(self, value):
        self._linewidth_narrow = value

    @property
    def color_cycle(self):
        if hasattr(self, '_color_cycle'):
            return self._color_cycle
        else:
            return mpl.rcParams['axes.prop_cycle'].by_key()['color']

    @color_cycle.setter
    def color_cycle(self, value):
        if isinstance(value, collections.Iterable):
            mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=value)
        else:
            mpl.rcParams['axes.prop_cycle'] = value
        self._color_cycle = value

    @property
    def size_fraction_x(self):
        if hasattr(self, '_size_fraction_x'):
            return self._size_fraction_x
        else:
            return 1

    @property
    def size_fraction_y(self):
        if hasattr(self, '_size_fraction_y'):
            return self._size_fraction_y
        else:
            return 1

    @size_fraction_x.setter
    def size_fraction_x(self, value):
        self._size_fraction_x = value
        self._set_figure_dimensions()

    @size_fraction_y.setter
    def size_fraction_y(self, value):
        self._size_fraction_y = value
        self._set_figure_dimensions()

    @property
    def colormap(self):
        if hasattr(self, '_colormap'):
            return self._colormap
        else:
            return mpl.rcParams['image.cmap']

    @property
    def latex_preamble(self):
        if hasattr(self, '_latex_preamble'):
            return self._latex_preamble
        else:
            return mpl.rcParams['text.latex.preamble']

    @latex_preamble.setter
    def latex_preamble(self, value):
        matplotlib.rcParams['text.latex.preamble'] = value
        self._latex_preamble = value

    @property
    def usetex(self):
        if hasattr(self, '_usetex'):
            return self._usetex
        else:
            return mpl.rcParams['text.usetex']

    @usetex.setter
    def usetex(self, value):
        mpl.rcParams['text.usetex'] = value
        self._usetex = value

    @colormap.setter
    def colrmap(self, value):
        self._colormap = value
        mpl.rcParams['image.cmap']

    @property
    def markersize(self):
        if hasattr(self, '_markersize'):
            return self._markersize
        else:
            return mpl.rcParams['lines.markersize']

    @markersize.setter
    def markersize(self, value):
        mpl.rcParams['lines.markersize'] = value
        self._markersize = value

    @property
    def markeredgewidth(self):
        if hasattr(self, '_markeredgewidth'):
            return self._markeredgewidth
        else:
            return mpl.rcParams['lines.markeredgewidth']

    @markeredgewidth.setter
    def markeredgewidth(self, value):
        mpl.rcParams['lines.markeredgewidth'] = value
        self._markeredgewidth = value

    @property
    def alpha(self):
        if hasattr(self, '_alpha'):
            return self._alpha
        else:
            return 1

    @alpha.setter
    def alpha(self, value):
        self._alpha = value

    @property
    def capsize(self):
        if hasattr(self, '_capsize'):
            return self.capsize
        else:
            return mpl.rcParams["errorbar.capsize"]

    @capsize.setter
    def capsize(self, value):
        mpl.rcParams["errorbar.capsize"] = value
        self._capsize = value

    def _common_settings(self):
        self.usetex = False
        
        #self.rc_params = {'pdf.use14corefonts': True}
        #self.latex_preamble = [r'\usepackage{siunitx}', r'\usepackage{amsmath}', r'\usepackage{newtxmath}']
        #self.latex_preamble = [r'\usepackage{siunitx}', r'\usepackage{amsmath}', r'\usepackage[T1]{fontenc}', r'\fontfamily{qcr}\selectfont']
        #self.latex_preamble = [r'\usepackage{siunitx}', r'\usepackage{amsmath}']
        # mpl.rcParams.update({
        #     "text.usetex": True,
        #     "font.family": "serif",
        #     "font.serif": ["Palatino"],
        # })
        #self.latex_preamble = [r'\usepackage{siunitx}', r'\usepackage{amsmath}',  r'\usepackage{newtxmath}']

    def large(self):
        self._common_settings()
        self.fontsize = 15
        self.figure_size = 10
        self.aspect_ratio = 1.5
        #self.font = 'Times New Roman'
        self.font = 'Times New Roman'

    def nature_sc(self):
        self._common_settings()
        self.fontsize = 6 # must be between 5 and 7
        self.figure_size = 3.5
        self.font = 'Times New Roman'

    def nature_dc(self):
        self._common_settings()
        self.fontsize = 6
        self.figure_size = 6.1
        self.font = 'Times New Roman'

    def pr(self):
        self.fontsize = 6
        self.figure_size = 3 + 3/8
        self.font = 'Times New Roman'
        self.markersize = 3
        self.markeredgewidth = self.markersize/7
        self.linewidth = 1
        self.alpha = 0.7
        self.capsize = self.markersize
        self.size_fraction_x = 1
        self.size_fraction_y = 1
        #self.color_cycle = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
        self.color_cycle = [
            '#648fff',
            '#fe6100',
            '#dc267f',
            '#785ef0',
            '#ffb000',
            '#000000',
            '#ffffff',
        ]



    def pr_single_column(self):
        self.pr()
        self.figure_size = 3 + 3/8

    def pr_one_and_half_column(self):
        self.pr()
        self.figure_size = (3 + 3/8)*1.5

    def pr_double_column(self):
        self.pr()
        self.figure_size = (3 + 3/8)*2


    def anc_style(self):
        self.fontsize = 6
        self.figure_size = 6.1
        self.font = 'Times New Roman'
        self.markersize = 3
        self.markeredgewidth = self.markersize/7
        self.linewidth = 1
        self.alpha = 0.7
        self.capsize = self.markersize
        self.size_fraction_x = 1
        self.size_fraction_y = 1
        self.color_cycle = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
        #self.color_cycle = ['006BA4', 'FF800E', 'ABABAB', '595959', '5F9ED1', 'C85200', '898989', 'A2C8EC', 'FFBC79', 'CFCFCF']
        # self.color_cycle = ['#4c72b0',
        #                     '#dd8452',
        #                     '#55a868',
        #                     '#c44e52',
        #                     '#8172b3',
        #                     '#937860',
        #                     '#da8bc3',
        #                     '#8c8c8c',
        #                     '#ccb974',
        #                     '#64b5cd']
        #self.color_cycle = ['#f77189', '#ae9d31', '#33b07a', '#38a9c5', '#cc7af4']

    def presentation(self):
        self.fontsize = 16
        self.figure_size = 6.4
        #self.font = 'Times New Roman'
        self.markersize = 8
        self.markeredgewidth = self.markersize/7
        self.linewidth = 1.5
        self.axes_linewidth = 1.5
        self.alpha = 0.7
        self.aspect_ratio = 0.9
        self.size_fraction_x = 1
        self.size_fraction_y = 1
