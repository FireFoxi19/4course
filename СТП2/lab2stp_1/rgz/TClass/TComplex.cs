using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace calculator
{
    public class TComplex : ANumber
    {
        private double real;
        private double imaginary;
        const string Separator = " + i * ";

        public double Real
        {
            get
            {
                return real;
            }
            set
            {
                real = value;
            }
        }

        public double Imaginary
        {

            get
            {
                return imaginary;
            }
            set
            {
                imaginary = value;
            }
        }

        public TComplex()
        {
            real = 0;
            imaginary = 0;
        }

        public TComplex(int a, int b)
        {
            real = a;
            imaginary = b;
        }

        public TComplex(double a, double b)
        {
            real = a;
            imaginary = b;
        }
        public TComplex(TComplex complex)
        {
            real = complex.real;
            imaginary = complex.imaginary;
        }

        public TComplex(string str)
        {
            Regex FullNumber = new Regex(@"^-?(\d+.?\d*)\s+\+\s+i\s+\*\s+-?(\d+.?\d*)$");
            Regex LeftPart = new Regex(@"^-?(\d+.?\d*)(\s+\+\s+i\s+\*\s+)?$");
            if (FullNumber.IsMatch(str))
            {
                List<string> Parts = str.Split(new string[] { Separator }, StringSplitOptions.None).ToList();

                real = Double.Parse(Parts[0]);
                imaginary = Double.Parse(Parts[1]);
            }
            else if (LeftPart.IsMatch(str))
            {
                if (str.Contains(Separator))
                    str = str.Replace(Separator, string.Empty);
                real = Double.Parse(str);
                imaginary = 0;
            }
            else
            {
                real = 0;
                imaginary = 0;
            }
        }

        public TComplex Copy()
        {
            return (TComplex)this.MemberwiseClone();
        }

        public TComplex Add(TComplex b)
        {
            TComplex res = this.Copy();
            res.real += b.real;
            res.imaginary += b.imaginary;
            return res;
        }

        public TComplex Sub(TComplex b)
        {
            TComplex res = this.Copy();
            res.real -= b.real;
            res.imaginary -= b.imaginary;
            return res;
        }

        public TComplex Mul(TComplex b)
        {
            TComplex res = this.Copy();
            res.real = this.real * b.real - this.imaginary * b.imaginary;
            res.imaginary = this.real * b.imaginary + this.imaginary * b.real;
            return res;
        }

        public TComplex Div(TComplex b)
        {
            TComplex res = this.Copy();
            res.real = (this.real * b.real + this.imaginary * b.imaginary) / (b.real * b.real + b.imaginary * b.imaginary);
            res.imaginary = (b.real * this.imaginary - this.real * b.imaginary) / (b.real * b.real + b.imaginary * b.imaginary);
            return res;
        }

        public TComplex Square()
        {
            TComplex res = this.Copy();
            res.real = this.real * this.real - this.imaginary * this.imaginary;
            res.imaginary = this.real * this.imaginary + this.real * this.imaginary;
            return res;
        }

        public TComplex Reverse()
        {
            TComplex res = this.Copy();
            res.real = this.real / (this.real * this.real + this.imaginary * this.imaginary);
            res.imaginary = -this.imaginary / (this.real * this.real + this.imaginary * this.imaginary);
            return res;
        }

        public TComplex Minus()
        {
            TComplex res = this.Copy();
            res.real = 0 - res.real;
            res.imaginary = 0 - res.imaginary;
            return res;
        }

        public double Abs()
        {
            return Math.Sqrt(this.real * this.real + this.imaginary * this.imaginary);
        }

        public double Rad()
        {
            if (this.real > 0)
                return Math.Atan(this.imaginary / this.real);

            if (this.real == 0 && this.imaginary > 0)
                return (Math.PI / 2);

            if (this.real < 0)
                return (Math.Atan(this.imaginary / this.real) + Math.PI);

            if (this.real == 0 && this.imaginary < 0)
                return (-Math.PI / 2);

            return 0;
        }

        public double Degree()
        {
            return Rad() * 180 / Math.PI;
        }

        public TComplex Pow(int n)
        {
            TComplex res = this.Copy();
            res.real = Math.Pow(Abs(), n) * Math.Cos(n * Rad());
            res.imaginary = Math.Pow(Abs(), n) * Math.Sin(n * Rad());
            return res;
        }

        public TComplex Sqrt(int powN, int rootI)
        {
            if (rootI >= powN || rootI < 0 || powN < 0)
                return new TComplex();
            return new TComplex(Math.Pow(Abs(), 1.0 / powN) * Math.Cos((Degree() + 2 * Math.PI * rootI) / powN), Math.Pow(Abs(), 1.0 / powN) * Math.Sin((Degree() + 2 * Math.PI * rootI) / powN));
        }

        public bool Equal(TComplex anClass)
        {
            return (this.real == anClass.real && this.imaginary == anClass.imaginary);
        }

        public bool NotEqual(TComplex anClass)
        {
            return (this.real != anClass.real || this.imaginary != anClass.imaginary);
        }

        public double GetRealNumber()
        {
            return this.real;
        }

        public double GetImaginaryNumber()
        {
            return this.imaginary;
        }

        public string GetRealString()
        {
            return this.real.ToString();
        }

        public string GetImaginaryString()
        {
            return this.imaginary.ToString();
        }
        
        public override void SetString(string str) {
            TComplex temp = new TComplex(str);
            Real = temp.Real;
            Imaginary = temp.Imaginary;
        }

        public override string ToString()
        {
            return GetRealString() + " + i * " + GetImaginaryString();
        }
    }
}
