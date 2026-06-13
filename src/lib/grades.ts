// Grade and topic data for MathPractice K5
// Single source of truth for all page generation

export interface Topic {
  id: string;
  name: string;
  description: string;
  icon: string;
  bgColor: string;
  worksheetCount: number;
  difficulty: 'Easy' | 'Medium' | 'Hard';
  seoH1: string;
  seoDescription: string;
}

export interface GradeData {
  id: string;
  label: string;
  name: string;
  color: string;
  description: string;
  seoH1: string;
  seoDescription: string;
  topics: Topic[];
}

export const grades: GradeData[] = [
  {
    id: 'k',
    label: 'K',
    name: 'Kindergarten',
    color: '#0075de',
    description: 'Counting, number recognition, shapes, and basic patterns for Kindergarten students.',
    seoH1: 'Free Kindergarten Math Worksheets — Printable PDFs',
    seoDescription: 'Free printable kindergarten math worksheets. Practice counting, number recognition, shapes, patterns, and more. PDF format, ready to print.',
    topics: [
      { id: 'counting', name: 'Counting', description: 'Count objects, numbers 1–20, and number sequences.', icon: '🔢', bgColor: '#e3f2fd', worksheetCount: 5, difficulty: 'Easy', seoH1: 'Free Kindergarten Counting Worksheets', seoDescription: 'Free printable kindergarten counting worksheets. Count objects, numbers 1-20, and practice number sequences.' },
      { id: 'number-recognition', name: 'Number Recognition', description: 'Identify and write numbers 0–20.', icon: '🔟', bgColor: '#e8f5e9', worksheetCount: 4, difficulty: 'Easy', seoH1: 'Free Number Recognition Worksheets for Kindergarten', seoDescription: 'Free printable number recognition worksheets for kindergarten. Identify and write numbers 0-20.' },
      { id: 'shapes', name: 'Shapes', description: 'Identify basic shapes: circles, squares, triangles, rectangles.', icon: '⬛', bgColor: '#fff3e0', worksheetCount: 4, difficulty: 'Easy', seoH1: 'Free Kindergarten Shapes Worksheets', seoDescription: 'Free printable shapes worksheets for kindergarten. Identify circles, squares, triangles, and rectangles.' },
      { id: 'patterns', name: 'Patterns', description: 'Complete and create simple patterns with shapes and colors.', icon: '🔁', bgColor: '#f3e5f5', worksheetCount: 3, difficulty: 'Easy', seoH1: 'Free Pattern Worksheets for Kindergarten', seoDescription: 'Free printable pattern worksheets for kindergarten. Practice completing and creating simple patterns.' },
      { id: 'comparing-numbers', name: 'Comparing Numbers', description: 'Compare numbers using greater than, less than, and equal to.', icon: '⚖️', bgColor: '#fce4ec', worksheetCount: 4, difficulty: 'Medium', seoH1: 'Free Comparing Numbers Worksheets for Kindergarten', seoDescription: 'Free printable comparing numbers worksheets for kindergarten. Practice greater than, less than, and equal to.' },
    ],
  },
  {
    id: '1',
    label: '1',
    name: 'Grade 1',
    color: '#2e7d32',
    description: 'Addition, subtraction, place value, and telling time for first graders.',
    seoH1: 'Free Grade 1 Math Worksheets — Printable PDFs',
    seoDescription: 'Free printable grade 1 math worksheets. Practice addition, subtraction, place value, telling time, and more. PDF format, ready to print.',
    topics: [
      { id: 'addition', name: 'Addition', description: 'Single-digit and two-digit addition within 20.', icon: '➕', bgColor: '#e8f5e9', worksheetCount: 5, difficulty: 'Easy', seoH1: 'Free Grade 1 Addition Worksheets', seoDescription: 'Free printable grade 1 addition worksheets. Practice single-digit and two-digit addition within 20.' },
      { id: 'subtraction', name: 'Subtraction', description: 'Single-digit subtraction within 20.', icon: '➖', bgColor: '#fce4ec', worksheetCount: 5, difficulty: 'Easy', seoH1: 'Free Grade 1 Subtraction Worksheets', seoDescription: 'Free printable grade 1 subtraction worksheets. Practice single-digit subtraction within 20.' },
      { id: 'place-value', name: 'Place Value', description: 'Tens and ones — understanding the base-10 system.', icon: '🔢', bgColor: '#f3e5f5', worksheetCount: 4, difficulty: 'Medium', seoH1: 'Free Grade 1 Place Value Worksheets', seoDescription: 'Free printable grade 1 place value worksheets. Practice tens and ones with the base-10 system.' },
      { id: 'time', name: 'Telling Time', description: 'Tell time to the hour and half-hour on analog clocks.', icon: '⏰', bgColor: '#fff3e0', worksheetCount: 4, difficulty: 'Medium', seoH1: 'Free Grade 1 Telling Time Worksheets', seoDescription: 'Free printable grade 1 telling time worksheets. Practice telling time to the hour and half-hour.' },
      { id: 'money', name: 'Money Math', description: 'Identify coins and count pennies, nickels, and dimes.', icon: '💰', bgColor: '#e3f2fd', worksheetCount: 4, difficulty: 'Medium', seoH1: 'Free Grade 1 Money Worksheets', seoDescription: 'Free printable grade 1 money math worksheets. Identify coins and count pennies, nickels, and dimes.' },
      { id: 'word-problems', name: 'Word Problems', description: 'Simple addition and subtraction word problems.', icon: '📝', bgColor: '#e8f5e9', worksheetCount: 3, difficulty: 'Hard', seoH1: 'Free Grade 1 Math Word Problems Worksheets', seoDescription: 'Free printable grade 1 math word problems worksheets. Practice simple addition and subtraction word problems.' },
    ],
  },
  {
    id: '2',
    label: '2',
    name: 'Grade 2',
    color: '#e65100',
    description: 'Two-digit operations, measurement, money math, and more for second graders.',
    seoH1: 'Free Grade 2 Math Worksheets — Printable PDFs',
    seoDescription: 'Free printable grade 2 math worksheets. Practice two-digit addition and subtraction, measurement, money math, and more. PDF format.',
    topics: [
      { id: 'addition', name: 'Addition', description: 'Two-digit addition with and without regrouping.', icon: '➕', bgColor: '#e8f5e9', worksheetCount: 5, difficulty: 'Medium', seoH1: 'Free Grade 2 Addition Worksheets — Two-Digit Addition', seoDescription: 'Free printable grade 2 addition worksheets. Practice two-digit addition with and without regrouping.' },
      { id: 'subtraction', name: 'Subtraction', description: 'Two-digit subtraction with and without borrowing.', icon: '➖', bgColor: '#fce4ec', worksheetCount: 5, difficulty: 'Medium', seoH1: 'Free Grade 2 Subtraction Worksheets — Two-Digit Subtraction', seoDescription: 'Free printable grade 2 subtraction worksheets. Practice two-digit subtraction with and without borrowing.' },
      { id: 'place-value', name: 'Place Value', description: 'Hundreds, tens, and ones — expanded form and comparisons.', icon: '🔢', bgColor: '#f3e5f5', worksheetCount: 4, difficulty: 'Medium', seoH1: 'Free Grade 2 Place Value Worksheets', seoDescription: 'Free printable grade 2 place value worksheets. Practice hundreds, tens, ones, expanded form, and comparisons.' },
      { id: 'measurement', name: 'Measurement', description: 'Measure length in inches, feet, centimeters, and meters.', icon: '📏', bgColor: '#e3f2fd', worksheetCount: 4, difficulty: 'Medium', seoH1: 'Free Grade 2 Measurement Worksheets', seoDescription: 'Free printable grade 2 measurement worksheets. Practice measuring length in inches, feet, centimeters, and meters.' },
      { id: 'money', name: 'Money Math', description: 'Count coins and bills, make change up to $5.', icon: '💰', bgColor: '#fff3e0', worksheetCount: 4, difficulty: 'Hard', seoH1: 'Free Grade 2 Money Math Worksheets', seoDescription: 'Free printable grade 2 money math worksheets. Practice counting coins and bills, and making change.' },
      { id: 'time', name: 'Telling Time', description: 'Tell time to 5-minute intervals on analog clocks.', icon: '⏰', bgColor: '#e8f5e9', worksheetCount: 3, difficulty: 'Medium', seoH1: 'Free Grade 2 Telling Time Worksheets', seoDescription: 'Free printable grade 2 telling time worksheets. Practice telling time to 5-minute intervals.' },
    ],
  },
  {
    id: '3',
    label: '3',
    name: 'Grade 3',
    color: '#6a1b9a',
    description: 'Multiplication, division, fractions basics, and geometry for third graders.',
    seoH1: 'Free Grade 3 Math Worksheets — Printable PDFs',
    seoDescription: 'Free printable grade 3 math worksheets. Practice multiplication, division, fractions, geometry, and more. PDF format, ready to print.',
    topics: [
      { id: 'multiplication', name: 'Multiplication', description: 'Multiplication facts 0–12 and basic multi-digit multiplication.', icon: '✖️', bgColor: '#f3e5f5', worksheetCount: 5, difficulty: 'Medium', seoH1: 'Free Grade 3 Multiplication Worksheets', seoDescription: 'Free printable grade 3 multiplication worksheets. Practice multiplication facts 0-12 and basic multi-digit multiplication.' },
      { id: 'division', name: 'Division', description: 'Division facts 0–12 and basic division problems.', icon: '➗', bgColor: '#fff3e0', worksheetCount: 5, difficulty: 'Medium', seoH1: 'Free Grade 3 Division Worksheets', seoDescription: 'Free printable grade 3 division worksheets. Practice division facts 0-12 and basic division problems.' },
      { id: 'fractions', name: 'Fractions Basics', description: 'Identify, compare, and shade fractions (1/2, 1/3, 1/4).', icon: '🍕', bgColor: '#e3f2fd', worksheetCount: 5, difficulty: 'Medium', seoH1: 'Free Grade 3 Fractions Worksheets', seoDescription: 'Free printable grade 3 fractions worksheets. Practice identifying, comparing, and shading basic fractions.' },
      { id: 'addition', name: 'Addition', description: 'Three-digit addition with regrouping.', icon: '➕', bgColor: '#e8f5e9', worksheetCount: 4, difficulty: 'Medium', seoH1: 'Free Grade 3 Addition Worksheets', seoDescription: 'Free printable grade 3 addition worksheets. Practice three-digit addition with regrouping.' },
      { id: 'subtraction', name: 'Subtraction', description: 'Three-digit subtraction with borrowing.', icon: '➖', bgColor: '#fce4ec', worksheetCount: 4, difficulty: 'Medium', seoH1: 'Free Grade 3 Subtraction Worksheets', seoDescription: 'Free printable grade 3 subtraction worksheets. Practice three-digit subtraction with borrowing.' },
      { id: 'geometry', name: 'Geometry', description: 'Identify shapes, perimeter, and area of rectangles.', icon: '📐', bgColor: '#e8f5e9', worksheetCount: 4, difficulty: 'Hard', seoH1: 'Free Grade 3 Geometry Worksheets', seoDescription: 'Free printable grade 3 geometry worksheets. Practice identifying shapes, perimeter, and area of rectangles.' },
      { id: 'word-problems', name: 'Word Problems', description: 'Multiplication, division, and two-step word problems.', icon: '📝', bgColor: '#f3e5f5', worksheetCount: 3, difficulty: 'Hard', seoH1: 'Free Grade 3 Math Word Problems Worksheets', seoDescription: 'Free printable grade 3 math word problems worksheets. Practice multiplication, division, and two-step word problems.' },
    ],
  },
  {
    id: '4',
    label: '4',
    name: 'Grade 4',
    color: '#c62828',
    description: 'Multi-digit operations, equivalent fractions, and angles for fourth graders.',
    seoH1: 'Free Grade 4 Math Worksheets — Printable PDFs',
    seoDescription: 'Free printable grade 4 math worksheets. Practice multi-digit operations, equivalent fractions, angles, geometry, and more. PDF format.',
    topics: [
      { id: 'fractions', name: 'Fractions', description: 'Equivalent fractions, comparing fractions, and adding/subtracting fractions.', icon: '🍕', bgColor: '#e3f2fd', worksheetCount: 5, difficulty: 'Medium', seoH1: 'Free Grade 4 Fractions Worksheets', seoDescription: 'Free printable grade 4 fractions worksheets. Practice equivalent fractions, comparing fractions, and adding/subtracting fractions.' },
      { id: 'multiplication', name: 'Multiplication', description: 'Multi-digit multiplication (2-digit × 2-digit).', icon: '✖️', bgColor: '#f3e5f5', worksheetCount: 5, difficulty: 'Hard', seoH1: 'Free Grade 4 Multiplication Worksheets', seoDescription: 'Free printable grade 4 multiplication worksheets. Practice multi-digit multiplication (2-digit by 2-digit).' },
      { id: 'division', name: 'Division', description: 'Long division with remainders.', icon: '➗', bgColor: '#fff3e0', worksheetCount: 5, difficulty: 'Hard', seoH1: 'Free Grade 4 Division Worksheets', seoDescription: 'Free printable grade 4 division worksheets. Practice long division with remainders.' },
      { id: 'addition', name: 'Addition', description: 'Multi-digit addition (4-digit and 5-digit numbers).', icon: '➕', bgColor: '#e8f5e9', worksheetCount: 4, difficulty: 'Medium', seoH1: 'Free Grade 4 Addition Worksheets', seoDescription: 'Free printable grade 4 addition worksheets. Practice multi-digit addition with 4-digit and 5-digit numbers.' },
      { id: 'subtraction', name: 'Subtraction', description: 'Multi-digit subtraction (4-digit and 5-digit numbers).', icon: '➖', bgColor: '#fce4ec', worksheetCount: 4, difficulty: 'Medium', seoH1: 'Free Grade 4 Subtraction Worksheets', seoDescription: 'Free printable grade 4 subtraction worksheets. Practice multi-digit subtraction with 4-digit and 5-digit numbers.' },
      { id: 'geometry', name: 'Geometry', description: 'Angles, lines of symmetry, and classifying shapes.', icon: '📐', bgColor: '#e8f5e9', worksheetCount: 4, difficulty: 'Medium', seoH1: 'Free Grade 4 Geometry Worksheets', seoDescription: 'Free printable grade 4 geometry worksheets. Practice angles, lines of symmetry, and classifying shapes.' },
      { id: 'word-problems', name: 'Word Problems', description: 'Multi-step word problems with all operations.', icon: '📝', bgColor: '#f3e5f5', worksheetCount: 3, difficulty: 'Hard', seoH1: 'Free Grade 4 Math Word Problems Worksheets', seoDescription: 'Free printable grade 4 math word problems worksheets. Practice multi-step word problems with all operations.' },
    ],
  },
  {
    id: '5',
    label: '5',
    name: 'Grade 5',
    color: '#004d40',
    description: 'Decimals, fractions operations, volume, and order of operations for fifth graders.',
    seoH1: 'Free Grade 5 Math Worksheets — Printable PDFs',
    seoDescription: 'Free printable grade 5 math worksheets. Practice decimals, fraction operations, volume, order of operations, and more. PDF format.',
    topics: [
      { id: 'decimals', name: 'Decimals', description: 'Read, write, compare, and round decimals to thousandths.', icon: '🔟', bgColor: '#f3e5f5', worksheetCount: 5, difficulty: 'Medium', seoH1: 'Free Grade 5 Decimals Worksheets', seoDescription: 'Free printable grade 5 decimals worksheets. Practice reading, writing, comparing, and rounding decimals.' },
      { id: 'fractions-and-decimals', name: 'Fractions & Decimals', description: 'Convert between fractions and decimals.', icon: '📊', bgColor: '#fff3e0', worksheetCount: 5, difficulty: 'Medium', seoH1: 'Free Grade 5 Converting Fractions and Decimals Worksheets', seoDescription: 'Free printable grade 5 fractions and decimals worksheets. Practice converting between fractions and decimals.' },
      { id: 'fractions', name: 'Fraction Operations', description: 'Add, subtract, multiply, and divide fractions.', icon: '🍕', bgColor: '#e3f2fd', worksheetCount: 5, difficulty: 'Hard', seoH1: 'Free Grade 5 Fraction Operations Worksheets', seoDescription: 'Free printable grade 5 fraction operations worksheets. Practice adding, subtracting, multiplying, and dividing fractions.' },
      { id: 'multiplication', name: 'Multiplication', description: 'Multi-digit multiplication and multiplication with decimals.', icon: '✖️', bgColor: '#f3e5f5', worksheetCount: 4, difficulty: 'Hard', seoH1: 'Free Grade 5 Multiplication Worksheets', seoDescription: 'Free printable grade 5 multiplication worksheets. Practice multi-digit multiplication and multiplication with decimals.' },
      { id: 'division', name: 'Division', description: 'Long division with decimals and multi-digit divisors.', icon: '➗', bgColor: '#fff3e0', worksheetCount: 4, difficulty: 'Hard', seoH1: 'Free Grade 5 Division Worksheets', seoDescription: 'Free printable grade 5 division worksheets. Practice long division with decimals and multi-digit divisors.' },
      { id: 'volume', name: 'Volume', description: 'Calculate volume of rectangular prisms (cubic units).', icon: '📦', bgColor: '#e8f5e9', worksheetCount: 4, difficulty: 'Medium', seoH1: 'Free Grade 5 Volume Worksheets', seoDescription: 'Free printable grade 5 volume worksheets. Practice calculating the volume of rectangular prisms.' },
      { id: 'order-of-operations', name: 'Order of Operations', description: 'Solve expressions using PEMDAS/GEMDAS rules.', icon: '🧮', bgColor: '#fce4ec', worksheetCount: 3, difficulty: 'Hard', seoH1: 'Free Grade 5 Order of Operations Worksheets', seoDescription: 'Free printable grade 5 order of operations worksheets. Practice solving expressions using PEMDAS/GEMDAS rules.' },
    ],
  },
];

export function getGrade(id: string): GradeData | undefined {
  return grades.find((g) => g.id === id);
}

export function getTopic(gradeId: string, topicId: string): Topic | undefined {
  const grade = getGrade(gradeId);
  return grade?.topics.find((t) => t.id === topicId);
}
