module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      screens: {
        'xs': {
          'max': '639px'
        },
        'sm': '640px',
        'md': '768px',
        'lg': '1024px',
        'xl': '1280px',
      },
      width: {
        '7': '1.75rem',
        '14': '3.5rem',
        '18': '4.5rem',
        '24': '6rem',
        '28': '7rem',
        '36': '9rem',
        '44': '11rem',
        '52': '13rem',
        '56': '14rem',
        '60': '15rem',
        '68': '17rem',
        '72': '18rem',
        '76': '19rem',
        '80': '20rem',
        '84': '21rem',
        '88': '22rem',
        '92': '23rem',
        '96': '24rem',
        '100': '25rem',
        '104': '26rem',
        '108': '27rem',
        '112': '28rem',
        '116': '29rem',
        '120': '30rem',
        '124': '31rem',
        '128': '32rem',
        '132': '33rem',
        '136': '34rem',
        '140': '35rem',
        '144': '36rem',
        '148': '37rem',
        '150': '37.5rem',
        '152': '38rem',
        '156': '39rem',
        '160': '40rem',
        '164': '41rem',
        '168': '42rem',
        '172': '43rem',
        '176': '44rem',
        '180': '45rem',
        '184': '46rem',
        '188': '47rem',
        '192': '48rem',
        '196': '49rem',
        '200': '50rem',
      },
      height: {
        '7': '1.75rem',
        '14': '3.5rem',
        '18': '4.5rem',
        '24': '6rem',
        '28': '7rem',
        '36': '9rem',
        '44': '11rem',
        '52': '13rem',
        '56': '14rem',
        '60': '15rem',
        '68': '17rem',
        '72': '18rem',
        '76': '19rem',
        '80': '20rem',
        '84': '21rem',
        '88': '22rem',
        '92': '23rem',
        '96': '24rem',
        '100': '25rem',
        '104': '26rem',
        '108': '27rem',
        '112': '28rem',
        '116': '29rem',
        '120': '30rem',
        '124': '31rem',
        '128': '32rem',
        '132': '33rem',
        '136': '34rem',
        '140': '35rem',
        '144': '36rem',
        '148': '37rem',
        '150': '37.5rem',
        '152': '38rem',
        '156': '39rem',
        '160': '40rem',
        '164': '41rem',
        '168': '42rem',
        '172': '43rem',
        '176': '44rem',
        '180': '45rem',
        '184': '46rem',
        '188': '47rem',
        '192': '48rem',
        '196': '49rem',
        '200': '50rem',
      },
      padding: {
        '-9': '-2.25rem',
        '-11': '-2.75rem',
        '11': '2.75rem',
        '14': '3.5rem',
        '28': '7rem',
      },
      margin: {
        '-9': '-2.25rem',
        '-11': '-2.75rem',
        '11': '2.75rem',
        '14': '3.5rem',
        '28': '7rem',
      },
    },
    boxShadow: {
      xs: '0 0 0 1px rgba(0, 0, 0, 0.05)',
      sm: '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
      default: '0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06)',
      md: '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
      lg: '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)',
      xl: '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)',
      '2xl': '0 25px 50px -12px rgba(0, 0, 0, 0.25)',
      '3xl': '0 35px 60px -15px rgba(0, 0, 0, 0.3)',
      inner: 'inset 0 2px 4px 0 rgba(0, 0, 0, 0.06)',
      focus: '0 0 0 3px rgba(66, 153, 225, 0.5)',
      none: 'none',
      msg: '0px 2px 10px 1px rgba(255, 255, 255, 0.25)',
    },
    fontSize: {
      'xxs': '.65rem',
      'xs': '.75rem',
      's': '0.825rem',
      'sm': '.875rem',
      'tiny': '.925rem',
      'base': '1rem',
      'lg': '1.125rem',
      'xl': '1.25rem',
      '2xl': '1.5rem',
      '3xl': '1.875rem',
      '4xl': '2.25rem',
      '5xl': '3rem',
      '6xl': '4rem',
      '7xl': '5rem',
    },
    opacity: {
      '0': '0',
      '25': '.25',
      '50': '.5',
      '75': '.75',
      '10': '.1',
      '20': '.2',
      '30': '.3',
      '40': '.4',
      '50': '.5',
      '60': '.6',
      '70': '.7',
      '80': '.8',
      '90': '.9',
      '100': '1',
    }
  },
  variants: {
    backgroundColor: ['responsive', 'hover', 'group-hover', 'focus', 'focus-within', 'active'],
    backgroundOpacity: ['responsive', 'hover', 'focus', 'active', 'group-hover'],
    borderColor: ['responsive', 'hover', 'group-hover', 'focus', 'focus-within', 'active'],
    textColor: ['responsive', 'hover', 'group-hover', 'focus', 'focus-within', 'active'],
    stroke: ['responsive', 'hover', 'focus', 'active'],
    fill: ['responsive', 'hover', 'focus', 'active'],
    strokeWidth: ['responsive', 'hover', 'focus', 'active'],
    visibility: ['responsive', 'hover', 'focus'],
  },
  plugins: [
    require('@tailwindcss/custom-forms')
  ],

}