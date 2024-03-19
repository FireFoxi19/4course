using Microsoft.VisualStudio.TestTools.UnitTesting;
using Converter;

namespace ConverterTestProj
{
    [TestClass]
    public class Test_ADT_Convert_10_p
    {
        [TestMethod]
        public void TestConvertControllerDecimalP()
        {
            double n = 123.123;
            int p = 12;
            int c = 3;
            string Expect = "A3.158";
            string Actual = Converter.ConvertControllerDecimalP.Do(n, p, c);
            Assert.AreEqual(Expect, Actual);
        }

        [TestMethod]
        public void TestConvertControllerDecimalP1()
        {
            double n = -144.523;
            int p = 3;
            int c = 8;
            string Expect = "-12100.11201002";
            string Actual = Converter.ConvertControllerDecimalP.Do(n, p, c);
            Assert.AreEqual(Expect, Actual);
        }

        [TestMethod]
        [ExpectedException(typeof(System.IndexOutOfRangeException))]
        public void TestConvertControllerDecimalP2()
        {
            double n = -12312.1231;
            int p = -3;
            int c = 8;
            string Actual = Converter.ConvertControllerDecimalP.Do(n, p, c);
        }

        [TestMethod]
        [ExpectedException(typeof(System.IndexOutOfRangeException))]
        public void TestConvertControllerDecimalP3()
        {
            double n = -12312.1231;
            int p = -3;
            int c = 8;
            string Actual = Converter.ConvertControllerDecimalP.Do(n, p, c);
        }

        [TestMethod]
        public void TestConvertControllerDecimalP4()
        {
            int n = 12;
            char ExpectedChar = 'C';
            char ActualChar = Converter.ConvertControllerDecimalP.Int—har(n);
            Assert.AreEqual(ExpectedChar, ActualChar);
        }

        [TestMethod]
        public void TestConvertControllerDecimalP5()
        {
            int n = 3;
            char ExpectedChar = '3';
            char ActualChar = Converter.ConvertControllerDecimalP.Int—har(n);
            Assert.AreEqual(ExpectedChar, ActualChar);
        }

        [TestMethod]
        [ExpectedException(typeof(System.IndexOutOfRangeException))]
        public void TestConvertControllerDecimalP6()
        {
            int n = -12;
            Converter.ConvertControllerDecimalP.Int—har(n);
        }

        [TestMethod]
        public void TestConvertControllerDecimalP7()
        {
            int n = 123;
            int p = 12;
            string ExpectedString = "A3";
            string ActualString = Converter.ConvertControllerDecimalP.IntP(n, p);
            Assert.AreEqual(ExpectedString, ActualString);
        }

        [TestMethod]
        public void TestConvertControllerDecimalP8()
        {
            int n = -234567;
            int p = 9;
            string ExpectedString = "-386680";
            string ActualString = Converter.ConvertControllerDecimalP.IntP(n, p);
            Assert.AreEqual(ExpectedString, ActualString);
        }

        [TestMethod]
        [ExpectedException(typeof(System.IndexOutOfRangeException))]
        public void TestConvertControllerDecimalP9()
        {
            int n = 123;
            int p = -24;
            string Actual = Converter.ConvertControllerDecimalP.IntP(n, p);
        }

        [TestMethod]
        public void TestConvertControllerDecimalP10()
        {
            double n = 0.123;
            int p = 12;
            int c = 3;
            string ExpectedString = "158";
            string ActualString = Converter.ConvertControllerDecimalP.DblP(n, p, c);
            Assert.AreEqual(ExpectedString, ActualString);
        }

        [TestMethod]
        public void TestConvertControllerDecimalP11()
        {
            double n = 0.417;
            int p = 9;
            int c = 5;
            string ExpectedString = "36688";
            string ActualString = Converter.ConvertControllerDecimalP.DblP(n, p, c);
            Assert.AreEqual(ExpectedString, ActualString);
        }


        [TestMethod]
        [ExpectedException(typeof(System.IndexOutOfRangeException))]
        public void TestConvertControllerDecimalP12()
        {
            double n = 1.5;
            int p = 12;
            int c = 3;
            string Actual = Converter.ConvertControllerDecimalP.DblP(n, p, c);
        }
    }


    [TestClass]
    public class Test_ADT_Convert_p_10
    {
        [TestMethod]
        public void TestConvertControllerPDecimal()
        {
            string Number = "123.321";
            int P = 4;
            double ExpectedValue = 27.890625;
            double ActualValue = Converter.ConvertControllerPDecimal.Dval(Number, P);
            Assert.AreEqual(ExpectedValue, ActualValue, 0.00001);
        }

        [TestMethod]
        public void TestConvertControllerPDecimal1()
        {
            string Number = "37.53";
            int P = 8;
            double ExpectedValue = 31.671875;
            double ActualValue = Converter.ConvertControllerPDecimal.Dval(Number, P);
            Assert.AreEqual(ExpectedValue, ActualValue, 0.00001);
        }

        [TestMethod]
        public void TestConvertControllerPDecimal2()
        {
            string Number = "A8F.9C9";
            int P = 16;
            double ExpectedValue = 2703.611572265625;
            double ActualValue = Converter.ConvertControllerPDecimal.Dval(Number, P);
            Assert.AreEqual(ExpectedValue, ActualValue, 0.00001);
        }

        [TestMethod]
        public void TestConvertControllerPDecimal3()
        {
            string Number = "0.23A5";
            int P = 13;
            double ExpectedValue = 0.17632435839081264662;
            double ActualValue = Converter.ConvertControllerPDecimal.Dval(Number, P);
            Assert.AreEqual(ExpectedValue, ActualValue, 0.00001);
        }

        [TestMethod]
        public void TestConvertControllerPDecimal4()
        {
            string Number = "9876";
            int P = 11;
            double ExpectedValue = 13030;
            double ActualValue = Converter.ConvertControllerPDecimal.Dval(Number, P);
            Assert.AreEqual(ExpectedValue, ActualValue, 0.00001);
        }

        [TestMethod]
        [ExpectedException(typeof(System.Exception))]
        public void TestConvertControllerPDecimal5()
        {
            string Number = ".A";
            int P = 11;
            Converter.ConvertControllerPDecimal.Dval(Number, P);
        }

        [TestMethod]
        [ExpectedException(typeof(System.IndexOutOfRangeException))]
        public void TestConvertControllerPDecimal6()
        {
            string Number = "AA";
            int P = 77;
            Converter.ConvertControllerPDecimal.Dval(Number, P);
        }

        [TestMethod]
        [ExpectedException(typeof(System.Exception))]
        public void TestConvertControllerPDecimal7()
        {
            string Number = "FFF";
            int P = 2;
            Converter.ConvertControllerPDecimal.Dval(Number, P);
        }
    }

    [TestClass]
    public class Test_Editor
    {
        [TestMethod]
        public void TestEditorController()
        {
            Converter.EditorController editor = new Converter.EditorController();
            editor.addDigit(0);
            string ExpectedValue = "0";
            string ActualValue = editor.getNumber();
            Assert.AreEqual(ExpectedValue, ActualValue);
        }

        [TestMethod]
        public void TestEditorController1()
        {
            Converter.EditorController editor = new Converter.EditorController();
            editor.addDigit(0);
            editor.addDigit(0);
            editor.addDigit(0);
            editor.addDigit(0);
            editor.addDigit(0);
            string ExpectedValue = "0";
            string ActualValue = editor.getNumber();
            Assert.AreEqual(ExpectedValue, ActualValue);
        }

        [TestMethod]
        public void TestEditorController2()
        {
            Converter.EditorController editor = new Converter.EditorController();
            editor.addDigit(0);
            editor.addDelim();
            editor.addDigit(0);
            editor.addDigit(0);
            editor.addDigit(0);
            editor.addDigit(0);
            string ExpectedValue = "0.0000";
            string ActualValue = editor.getNumber();
            Assert.AreEqual(ExpectedValue, ActualValue);
        }

        [TestMethod]
        public void TestEditorController3()
        {
            Converter.EditorController editor = new Converter.EditorController();
            editor.addDigit(15);
            editor.addDigit(12);
            editor.addDigit(1);
            editor.addDelim();
            editor.addDigit(1);
            editor.addDigit(9);
            string ExpectedValue = "FC1.19";
            string ActualValue = editor.getNumber();
            Assert.AreEqual(ExpectedValue, ActualValue);
        }

        [TestMethod]
        [ExpectedException(typeof(System.IndexOutOfRangeException))]
        public void TestEditorController4()
        {
            Converter.EditorController editor = new Converter.EditorController();
            editor.addDigit(17);
        }

        [TestMethod]
        [ExpectedException(typeof(System.IndexOutOfRangeException))]
        public void TestEditorController5()
        {
            Converter.EditorController editor = new Converter.EditorController();
            editor.addDigit(-12);
        }

        [TestMethod]
        public void TestEditorController6()
        {
            Converter.EditorController editor = new Converter.EditorController();
            editor.addDigit(15);
            editor.addDigit(12);
            editor.addDigit(1);
            editor.addDelim();
            editor.addDigit(1);
            editor.addDigit(9);
            int ExpectedValue = 2;
            int ActualValue = editor.acc();
            Assert.AreEqual(ExpectedValue, ActualValue);
        }

        [TestMethod]
        public void TestEditorController7()
        {
            Converter.EditorController editor = new Converter.EditorController();
            int ExpectedValue = 0;
            int ActualValue = editor.acc();
            Assert.AreEqual(ExpectedValue, ActualValue);
        }

        [TestMethod]
        public void TestEditorController8()
        {
            Converter.EditorController editor = new Converter.EditorController();
            editor.addDelim();
            editor.addDigit(1);
            editor.addDigit(9);
            editor.addDigit(9);
            editor.addDigit(9);
            editor.addDigit(9);
            int ExpectedValue = 5;
            int ActualValue = editor.acc();
            Assert.AreEqual(ExpectedValue, ActualValue);
        }

        [TestMethod]
        public void TestEditorController9()
        {
            Converter.EditorController editor = new Converter.EditorController();
            editor.addDigit(15);
            editor.addDigit(15);
            editor.addDigit(15);
            editor.addDelim();
            editor.addDelim();
            editor.addDelim();
            editor.addDigit(15);
            editor.addDigit(15);
            editor.addDigit(15);
            editor.addDelim();
            editor.addDelim();
            editor.addDelim();
            string ExpectedValue = "FFF.FFF";
            string ActualValue = editor.getNumber();
            Assert.AreEqual(ExpectedValue, ActualValue);
        }

        [TestMethod]
        public void TestEditorController10()
        {
            Converter.EditorController editor = new Converter.EditorController();
            editor.addDigit(0);
            editor.addDelim();
            editor.addDelim();
            editor.addDelim();
            editor.addDigit(0);
            editor.addDelim();
            editor.addDelim();
            editor.addDelim();
            string ExpectedValue = "0.0";
            string ActualValue = editor.getNumber();
            Assert.AreEqual(ExpectedValue, ActualValue);
        }

        [TestMethod]
        public void TestEditorController11()
        {
            Converter.EditorController editor = new Converter.EditorController();
            editor.addDelim();
            editor.addDelim();
            editor.addDelim();
            string ExpectedValue = "0.";
            string ActualValue = editor.getNumber();
            Assert.AreEqual(ExpectedValue, ActualValue);
        }

        [TestMethod]
        public void TestEditorController12()
        {
            Converter.EditorController editor = new Converter.EditorController();
            editor.bs();
            editor.bs();
            string ExpectedValue = "0";
            string ActualValue = editor.getNumber();
            Assert.AreEqual(ExpectedValue, ActualValue);
        }

        [TestMethod]
        public void TestEditorController13()
        {
            Converter.EditorController editor = new Converter.EditorController();
            editor.bs();
            editor.addDigit(1);
            editor.addDigit(2);
            editor.bs();
            string ExpectedValue = "1";
            string ActualValue = editor.getNumber();
            Assert.AreEqual(ExpectedValue, ActualValue);
        }

        [TestMethod]
        public void TestEditorController14()
        {
            Converter.EditorController editor = new Converter.EditorController();
            editor.addDigit(3);
            editor.addDigit(3);
            editor.addDigit(3);
            editor.addDelim();
            editor.bs();
            string ExpectedValue = "333";
            string ActualValue = editor.getNumber();
            Assert.AreEqual(ExpectedValue, ActualValue);
        }

        [TestMethod]
        public void TestEditorController15()
        {
            Converter.EditorController editor = new Converter.EditorController();
            editor.addDigit(3);
            editor.addDigit(3);
            editor.addDigit(3);
            editor.addDelim();
            editor.addDigit(3);
            editor.addDigit(3);
            editor.addDigit(3);
            editor.bs();
            editor.bs();
            editor.bs();
            string ExpectedValue = "333.";
            string ActualValue = editor.getNumber();
            Assert.AreEqual(ExpectedValue, ActualValue);
        }
    }

    [TestClass]
    public class Test_History
    {
        [TestMethod]
        public void TestHistoryController()
        {
            Converter.HistoryController history = new Converter.HistoryController();
            history.addRecord(12, 4, "23.42", "52.42");
            Converter.HistoryController.Record ExpectedValue = new Converter.HistoryController.Record(12, 4, "23.42", "52.42");
            Converter.HistoryController.Record ActualValue = history[0];
            Assert.AreEqual(ExpectedValue, ActualValue);
        }

        [TestMethod]
        public void TestHistoryController1()
        {
            Converter.HistoryController history = new Converter.HistoryController();
            history.addRecord(3, 7, "11.11", "11.11");
            Converter.HistoryController.Record ExpectedValue = new Converter.HistoryController.Record(3, 7, "11.11", "11.11");
            Converter.HistoryController.Record ActualValue = history[0];
            Assert.AreEqual(ExpectedValue, ActualValue);
        }

        [TestMethod]
        public void TestHistoryController2()
        {
            Converter.HistoryController history = new Converter.HistoryController();
            history.addRecord(12, 4, "23.42", "52.42");
            history.addRecord(12, 4, "23.42", "52.42");
            history.addRecord(12, 4, "11", "11");
            Converter.HistoryController.Record ExpectedValue = new Converter.HistoryController.Record(12, 4, "11", "11");
            Converter.HistoryController.Record ActualValue = history[2];
            Assert.AreEqual(ExpectedValue, ActualValue);
        }

        [TestMethod]
        public void TestHistoryController3()
        {
            Converter.HistoryController history = new Converter.HistoryController();
            history.addRecord(12, 4, "23.42", "52.42");
            history.addRecord(12, 4, "23.42", "52.42");
            history.addRecord(12, 4, "11", "11");
            Converter.HistoryController.Record ToOverride = new Converter.HistoryController.Record(1, 1, "1", "1");
            history[1] = ToOverride;
            Converter.HistoryController.Record ExpectedValue = new Converter.HistoryController.Record(1, 1, "1", "1");
            Converter.HistoryController.Record ActualValue = history[1];
            Assert.AreEqual(ExpectedValue, ActualValue);
        }

        [TestMethod]
        [ExpectedException(typeof(System.IndexOutOfRangeException))]
        public void TestHistoryController4()
        {
            Converter.HistoryController history = new Converter.HistoryController();
            history.addRecord(3, 7, "11.11", "11.11");
            Converter.HistoryController.Record Value = history[-1];
        }

        [TestMethod]
        [ExpectedException(typeof(System.IndexOutOfRangeException))]
        public void TestHistoryController5()
        {
            Converter.HistoryController history = new Converter.HistoryController();
            history.addRecord(3, 7, "11.11", "11.11");
            Converter.HistoryController.Record Value = history[1];
        }

        [TestMethod]
        [ExpectedException(typeof(System.IndexOutOfRangeException))]
        public void TestHistoryController6()
        {
            Converter.HistoryController history = new Converter.HistoryController();
            Converter.HistoryController.Record Value = new Converter.HistoryController.Record(12, 4, "11", "11");
            history[0] = Value;
        }
    }
}
