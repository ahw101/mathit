# -*- coding: utf-8 -*-
"""Guides: Calculating (written and recall methods)."""

CAT = "Calculating"

GUIDES = [

# ---------------------------------------------------------------- 1
dict(
    slug="column-addition", cat=CAT, nav="Column addition", read=5,
    h1="Column addition, including carrying",
    card="Line up the columns, add from the right, carry cleanly \u2014 and know why it works.",
    years="Years 3\u20136",
    seo="Column addition explained \u2014 carrying, decimals and large numbers | Math It!",
    desc="How to set out and complete column addition, including carrying, adding decimals, adding more than two numbers, and the four errors that cause most lost marks.",
    keywords="column addition, formal written addition, carrying addition, adding decimals column, KS2 addition method, year 4 column addition",
    intro="""<p>Column addition is the formal written method for adding numbers that are too big to
      hold in your head. It works because of place value: ones are added to ones, tens to tens, and
      anything that overflows is carried into the next column.</p>
      <p>It is usually the first formal method children fully master, which makes it worth getting
      genuinely neat \u2014 the habits formed here carry straight into subtraction, multiplication
      and division.</p>""",
    steps=[
        ("Line up the ones column",
         "<p>Not the left-hand edge. Write the numbers so the ones sit above the ones, tens above "
         "tens and so on. With decimals, line up the decimal points instead and the rest follows "
         "automatically.</p>"),
        ("Rule a line and add from the right",
         "<p>Start with the ones column, the rightmost one. Working right to left is what makes "
         "carrying possible.</p>"),
        ("Write the ones digit, carry the ten",
         "<p>If a column totals 10 or more, write only the ones digit of that total under the line "
         "and write the tens digit as a small 1 under the next column to the left.</p>"),
        ("Include the carry in the next column",
         "<p>Add it in as you go. The commonest error in the whole method is writing a carry and "
         "then ignoring it.</p>"),
        ("Check with an estimate",
         "<p>Round each number and add roughly. 4,856 + 2,397 is about 5,000 + 2,400 = 7,400, so an "
         "answer of 7,253 is plausible and an answer of 6,253 is not.</p>"),
    ],
    examples=[
        ("4,856 + 2,397",
         ["Ones: 6 + 7 = 13. Write 3, carry 1.",
          "Tens: 5 + 9 + 1 = 15. Write 5, carry 1.",
          "Hundreds: 8 + 3 + 1 = 12. Write 2, carry 1.",
          "Thousands: 4 + 2 + 1 = 7."],
         "7,253"),
        ("34.7 + 8.95",
         ["Line up the decimal points, not the digits.",
          "Fill the gap: write 34.70 so both numbers have two decimal places.",
          "Hundredths: 0 + 5 = 5. Tenths: 7 + 9 = 16, write 6 carry 1.",
          "Ones: 4 + 8 + 1 = 13, write 3 carry 1. Tens: 3 + 1 = 4.",
          "Bring the decimal point straight down."],
         "43.65"),
        ("127 + 48 + 356",
         ["Stack all three with the ones lined up.",
          "Ones: 7 + 8 + 6 = 21. Write 1, carry 2.",
          "Tens: 2 + 4 + 5 + 2 = 13. Write 3, carry 1.",
          "Hundreds: 1 + 3 + 1 = 5."],
         "531"),
    ],
    mistakes=[
        ("Lining the numbers up on the left when they have different digit counts.",
         "Align the ones column. 127 + 48 must put the 8 under the 7, not under the 1."),
        ("Writing the carry and then forgetting to add it.",
         "Add the carry <em>first</em> in the next column, before the main digits. It becomes automatic."),
        ("Ignoring the decimal point and treating 34.7 + 8.95 as 347 + 895.",
         "Line up the decimal points and pad with zeros so every number has the same number of decimal places."),
        ("Cramming the digits so columns drift.",
         "Use squared paper, or draw faint vertical lines. Most \u2018careless\u2019 errors are really alignment errors."),
    ],
    sections=[
        ("Why carrying works",
         """<p>Each column can only hold the digits 0 to 9. When the ones column reaches 13 you have
         one complete ten and three left over. The ten cannot stay where it is, so it is exchanged
         for a single unit in the tens column \u2014 that is the carried 1.</p>
         <p>Children who are told to \u201cput the little one underneath\u201d without this explanation
         tend to carry into the wrong column under pressure. Thirty seconds spent partitioning
         13 into 10 + 3 prevents it.</p>"""),
        ("Adding more than two numbers",
         """<p>The method is unchanged, but carries get bigger. Adding five numbers can produce a
         column total of 40-something, so you carry a 4, not a 1. Children who have only ever
         carried 1s find this unsettling \u2014 worth deliberately practising.</p>"""),
        ("When not to use it",
         """<p>Formal column addition is for numbers you cannot handle mentally. 300 + 400 does not
         need a column method, and neither does 199 + 56 (add 200, take off 1). Part of being good
         at arithmetic is choosing the cheaper route, so ask \u201ccould I do this in my head?\u201d
         before reaching for the pencil.</p>"""),
    ],
    faqs=[
        ("At what age is column addition taught?",
         "Formal column addition for three-digit numbers is a Year 3 objective in England, extended to four digits and beyond in Year 4, and to decimals in Years 5 and 6."),
        ("Should the carry go above or below the line?",
         "Either is accepted. UK schools usually write it small under the next column, which keeps the top line of the sum clean."),
        ("How do I add numbers with different decimal places?",
         "Pad the shorter one with trailing zeros so they match: 34.7 becomes 34.70. The value is unchanged and the columns line up."),
        ("Is column addition still worth teaching with calculators everywhere?",
         "Yes \u2014 it is assessed in KS2 SATs, and more importantly it is where children build a working understanding of place value and exchange."),
    ],
    cta=("Practise column addition", "practice.html?year=4&level=medium"),
    related=["column-subtraction", "place-value", "mental-strategies", "long-multiplication"],
),

# ---------------------------------------------------------------- 2
dict(
    slug="column-subtraction", cat=CAT, nav="Column subtraction", read=6,
    h1="Column subtraction and exchanging",
    card="The formal method including borrowing, and how to survive a row of zeros.",
    years="Years 3\u20136",
    seo="Column subtraction explained \u2014 exchanging, borrowing and zeros | Math It!",
    desc="Column subtraction step by step, including exchanging (borrowing), subtracting across zeros, decimal subtraction, and why you must never just take the smaller digit from the bigger one.",
    keywords="column subtraction, borrowing subtraction, exchanging subtraction, subtracting across zeros, KS2 subtraction method, year 4 column subtraction",
    intro="""<p>Column subtraction is the mirror of column addition, and it is noticeably harder.
      Addition only ever overflows; subtraction sometimes runs short, and then you have to go next
      door and break a ten.</p>
      <p>Schools call that exchanging; older books call it borrowing. The word does not matter.
      What matters is that the child understands they are swapping one ten for ten ones, not
      inventing a number.</p>""",
    steps=[
        ("Put the bigger number on top",
         "<p>Write the number being subtracted from on the top line, the amount being taken away "
         "underneath, ones column aligned.</p>"),
        ("Start at the ones and work left",
         "<p>Subtract the bottom digit from the top digit in each column, right to left.</p>"),
        ("If the top digit is too small, exchange",
         "<p>Take 1 from the column to the left. Cross out that digit, write it one smaller, and "
         "add 10 to the digit you are working on. 3 becomes 13.</p>"),
        ("Subtract from the new digit",
         "<p>Now the subtraction is possible. Write the result below the line and move left.</p>"),
        ("Zeros need a chain of exchanges",
         "<p>You cannot take 1 from a 0. Keep moving left until you find a non-zero digit, exchange "
         "there, and let each 0 become a 9 as the ten passes through it.</p>"),
    ],
    examples=[
        ("8,342 \u2212 2,567",
         ["Ones: 2 \u2212 7 won't go. Exchange from the tens: 4 becomes 3, ones become 12. 12 \u2212 7 = 5.",
          "Tens: 3 \u2212 6 won't go. Exchange from the hundreds: 3 becomes 2, tens become 13. 13 \u2212 6 = 7.",
          "Hundreds: 2 \u2212 5 won't go. Exchange from the thousands: 8 becomes 7, hundreds become 12. 12 \u2212 5 = 7.",
          "Thousands: 7 \u2212 2 = 5."],
         "5,775"),
        ("4,000 \u2212 1,268",
         ["Ones: 0 \u2212 8 won't go, and the tens and hundreds are both 0.",
          "Go left to the 4 thousands. 4 becomes 3.",
          "The ten passes through: hundreds 0 \u2192 9, tens 0 \u2192 9, ones 0 \u2192 10.",
          "Now: 10 \u2212 8 = 2, 9 \u2212 6 = 3, 9 \u2212 2 = 7, 3 \u2212 1 = 2."],
         "2,732"),
        ("12.4 \u2212 7.85",
         ["Pad to equal decimal places: 12.40 \u2212 7.85.",
          "Hundredths: 0 \u2212 5 won't go. Exchange: 4 becomes 3, hundredths become 10. 10 \u2212 5 = 5.",
          "Tenths: 3 \u2212 8 won't go. Exchange from the ones: 2 becomes 1, tenths become 13. 13 \u2212 8 = 5.",
          "Ones: 1 \u2212 7 won't go. Exchange from the tens: 1 becomes 0, ones become 11. 11 \u2212 7 = 4."],
         "4.55"),
    ],
    mistakes=[
        ("Taking the smaller digit from the bigger one regardless of position \u2014 doing 7 \u2212 2 when the sum says 2 \u2212 7.",
         "Subtraction is not commutative. If the top digit is smaller you must exchange, never flip the digits."),
        ("Exchanging but forgetting to reduce the column you took from.",
         "Every exchange has two halves: one column goes down by 1, the next goes up by 10. Cross out and rewrite both."),
        ("Stalling completely on 4,000 \u2212 1,268.",
         "Walk the exchange left until you reach a non-zero digit. Each zero on the way becomes a 9."),
        ("Not padding decimals, so 12.4 \u2212 7.85 loses a column.",
         "Write 12.40. Trailing zeros change nothing except the layout, and the layout is the whole point."),
    ],
    sections=[
        ("Exchanging versus borrowing",
         """<p>\u201cBorrowing\u201d implies you give it back, which you never do, and it leads to
         children writing a little 1 somewhere vague. \u201cExchanging\u201d is the modern term and
         it is accurate: one ten is swapped for ten ones. Same total, different arrangement.</p>
         <p>If your child was taught \u201cborrow and pay back\u201d (adding 1 to the bottom row
         instead of reducing the top), that method also works and is mathematically sound \u2014 but
         do not mix the two in one calculation.</p>"""),
        ("When counting on beats the column method",
         """<p>For subtractions where the numbers are close, counting on is faster and far less
         error-prone. 2,003 \u2212 1,987: count up from 1,987 to 2,000 (13), then 3 more. Answer 16,
         with no exchanges at all.</p>
         <p>The rule of thumb: if the two numbers are close together, count on. If they are far
         apart, use columns. Teaching both and letting the child choose is worth more than drilling
         either one alone.</p>"""),
        ("Checking by adding back",
         """<p>Subtraction has a built-in check. If 8,342 \u2212 2,567 = 5,775, then 5,775 + 2,567 must
         bring you back to 8,342. Addition is the easier operation, so the check is genuinely
         cheap \u2014 and it catches exchange errors that re-doing the subtraction would repeat.</p>"""),
    ],
    faqs=[
        ("Why does my child's school say \u2018exchange\u2019 instead of \u2018borrow\u2019?",
         "Because nothing is ever returned. Exchanging describes what actually happens: one ten is traded for ten ones."),
        ("What if the answer should be negative?",
         "Primary column subtraction always puts the larger number on top. Negative results are handled on a number line instead \u2014 see the negative numbers guide."),
        ("How do you subtract across several zeros?",
         "Move left to the first non-zero digit, reduce it by 1, and turn every zero you passed into a 9. The final column receives the 10."),
        ("Is the number line method acceptable in SATs?",
         "Yes, as long as the answer is right. Arithmetic papers only award method marks on a few multi-mark questions, and any valid method counts."),
    ],
    cta=("Practise column subtraction", "practice.html?year=4&level=medium"),
    related=["column-addition", "negative-numbers", "mental-strategies", "place-value"],
),

# ---------------------------------------------------------------- 3
dict(
    slug="times-tables", cat=CAT, nav="Times tables", read=7,
    h1="How to learn the times tables (and make them stick)",
    card="The order to learn them in, the patterns that halve the work, and what the Year 4 check involves.",
    years="Years 2\u20136",
    seo="How to learn the times tables \u2014 order, patterns and the Year 4 check | Math It!",
    desc="A practical plan for learning the times tables to 12 \u00d7 12: which order to teach them, the patterns in each table, how to practise division facts too, and what the Multiplication Tables Check involves.",
    keywords="times tables, learn times tables, times tables order, multiplication tables check, MTC year 4, times tables patterns, 7 times table, times tables practice",
    intro="""<p>By the end of Year 4 children in England are expected to recall every multiplication
      fact to 12 \u00d7 12 and the matching division facts. Recall, not work out \u2014 the national
      Multiplication Tables Check allows six seconds a question.</p>
      <p>That sounds brutal until you realise how much redundancy there is. Because 7 \u00d7 8 and
      8 \u00d7 7 are the same fact, and because the 1s, 2s, 5s and 10s are nearly free, there are only
      a few dozen genuinely new facts to learn.</p>""",
    steps=[
        ("Start with 10, 5 and 2",
         "<p>These have visible digit patterns. The 10s end in 0, the 5s alternate 5 and 0, the 2s "
         "are the even numbers. Most children arrive in Year 3 already knowing them.</p>"),
        ("Get the 4s and 8s by doubling",
         "<p>Double the 2s to reach the 4s, double the 4s to reach the 8s. 7 \u00d7 8 becomes "
         "7 \u00d7 2 = 14, \u00d7 2 = 28, \u00d7 2 = 56.</p>"),
        ("Do the 3s, then the 6s",
         "<p>The 6s are exactly double the 3s, so they come almost free: 6 \u00d7 7 is double "
         "3 \u00d7 7 = 21, so 42.</p>"),
        ("Use the 9s trick",
         "<p>9 \u00d7 n is 10 \u00d7 n minus n. 9 \u00d7 7 = 70 \u2212 7 = 63. The digits of every answer "
         "in the 9 times table add to 9, which makes checking instant.</p>"),
        ("Finish with 7, 11 and 12",
         "<p>By now most of these have already appeared inside other tables. The genuinely new ones "
         "are 7 \u00d7 7, 7 \u00d7 12 and 12 \u00d7 12. The 11s repeat the digit up to 9 \u00d7 11.</p>"),
        ("Practise the division direction",
         "<p>56 \u00f7 7 is the same fact asked backwards, and children who only rehearse forwards "
         "freeze on it. Mix division in as soon as a table is reasonably secure.</p>"),
    ],
    examples=[
        ("Work out 7 \u00d7 8 if you have forgotten it.",
         ["Use the 8s-by-doubling route.",
          "7 \u00d7 2 = 14.",
          "14 \u00d7 2 = 28.",
          "28 \u00d7 2 = 56."],
         "56"),
        ("Work out 9 \u00d7 6 using the 10s.",
         ["10 \u00d7 6 = 60.",
          "Take off one 6: 60 \u2212 6.",
          "Check: 5 + 4 = 9, so the digits confirm it is in the 9 times table."],
         "54"),
        ("Work out 12 \u00d7 7 by partitioning.",
         ["Split 12 into 10 and 2.",
          "10 \u00d7 7 = 70.",
          "2 \u00d7 7 = 14.",
          "70 + 14."],
         "84"),
        ("Work out 63 \u00f7 9.",
         ["Ask \u2018nine times what makes 63?\u2019",
          "Count up the 9s, or use 70 \u2212 7 = 63 to recognise 9 \u00d7 7."],
         "7"),
    ],
    mistakes=[
        ("Chanting the table from the start every time.",
         "Chanting builds sequence memory, not recall. Once the sequence is known, switch to random order questions \u2014 that is what the check and real life both demand."),
        ("Only ever practising multiplication.",
         "Half the curriculum requirement is the division facts. Drill 56 \u00f7 8 as hard as 7 \u00d7 8."),
        ("Treating 7 \u00d7 8 and 8 \u00d7 7 as two separate things to learn.",
         "Multiplication is commutative. Learning one gives you the other free \u2014 say both aloud together."),
        ("Practising for forty minutes once a week.",
         "Five minutes daily beats forty minutes weekly by a wide margin. Recall is built by frequency, not duration."),
    ],
    sections=[
        ("The Multiplication Tables Check",
         """<p>The MTC is taken online by all Year 4 children in England in June. It is 25 questions
         drawn from the 2 to 12 times tables, with six seconds to answer each and three seconds
         between questions. There is no pass mark published to parents and it is not used to stream
         children, but schools do see the data.</p>
         <p>The questions are multiplication only, weighted towards the 6s, 7s, 8s, 9s and 12s
         because those are the ones that need most work. Practising against a visible timer is
         therefore genuinely useful preparation \u2014 the format itself is part of the challenge.</p>"""),
        ("How many facts are actually new?",
         """<p>There are 121 facts in a 1\u201312 grid once you ignore the trivial 1s. Remove the
         reverses and you are down to about 66. Remove the 10s, 5s and 2s, and the 11s up to 9, and
         you are left with roughly 25 facts that require genuine effort. The notorious ones are
         6 \u00d7 7, 6 \u00d7 8, 7 \u00d7 8, 7 \u00d7 9, 8 \u00d7 9, 7 \u00d7 12 and 8 \u00d7 12.</p>
         <p>Framing it as \u201ctwenty-five hard facts\u201d rather than \u201ctwelve tables\u201d
         changes how achievable it feels.</p>"""),
        ("A six-week routine that works",
         """<p>Pick one table at a time. Monday: in order, multiplication only. Tuesday: shuffled.
         Wednesday: division only. Thursday: missing numbers (7 \u00d7 ? = 56). Friday: that table
         mixed with everything learned so far, timed. Move on when Friday is above 90% twice
         running.</p>
         <p>The <a href="../tables.html" class="link">times tables generator</a> does all five of
         those modes, so a week's practice is five clicks.</p>"""),
        ("Beyond 12",
         """<p>Tables above 12 are not required at primary, but they help: knowing 15 \u00d7 15 and
         25 \u00d7 4 speeds up percentages, and the squares to 15 are handy throughout secondary.
         Treat them as a bonus once the core grid is automatic, never as a substitute for it.</p>"""),
    ],
    faqs=[
        ("Which times table is hardest?",
         "The 7s, by common consent, because they have no digit pattern and appear least often elsewhere. 6 \u00d7 7, 7 \u00d7 8 and 7 \u00d7 9 are the three most-missed facts nationally."),
        ("How long should daily practice be?",
         "Five to ten minutes. Short and daily beats long and occasional, because recall is built by repeated retrieval rather than by time spent."),
        ("Should children use songs and chants?",
         "They are good for the first pass, but they build sequence memory. A child who has to sing from the start to reach 7 \u00d7 8 has not finished learning it \u2014 move to random-order questions."),
        ("What if my child is in Year 6 and still does not know them?",
         "Go back and fix it \u2014 it is worth the lost weeks. Nearly every Year 6 topic, from long division to simplifying fractions to percentages, is slowed down by shaky tables."),
    ],
    cta=("Open the times tables generator", "tables.html"),
    related=["long-multiplication", "short-division", "factors-multiples-primes", "number-bonds"],
),

# ---------------------------------------------------------------- 4
dict(
    slug="long-multiplication", cat=CAT, nav="Long multiplication", read=6,
    h1="Long multiplication: the column method",
    card="Multiply by a two-digit number without losing the placeholder zero.",
    years="Years 5\u20136",
    seo="Long multiplication explained \u2014 the column method step by step | Math It!",
    desc="Long multiplication set out clearly: multiplying by the ones, then the tens with its placeholder zero, adding the partial products, and handling decimals and three-digit multipliers.",
    keywords="long multiplication, column multiplication, multiply two digit numbers, long multiplication method, KS2 long multiplication, year 5 multiplication, grid method",
    intro="""<p>Long multiplication handles problems like 384 \u00d7 27 that are too big for mental
      methods. You split the multiplier into its place-value parts, multiply by each one separately,
      and add the results.</p>
      <p>There is exactly one thing that goes wrong, and it goes wrong constantly: the placeholder
      zero on the second line. Everything else is just times tables and column addition.</p>""",
    steps=[
        ("Set it out with the longer number on top",
         "<p>Write 384 above 27, ones column aligned, and rule a line underneath.</p>"),
        ("Multiply by the ones digit",
         "<p>7 \u00d7 384. Work right to left, carrying as you go, and write the whole answer on the "
         "first line under the rule.</p>"),
        ("Write the placeholder zero",
         "<p>Before you multiply by the tens digit, put a 0 in the ones column of the second line. "
         "You are about to multiply by 20, not by 2, and that zero is what records it.</p>"),
        ("Multiply by the tens digit",
         "<p>2 \u00d7 384, written to the left of the zero. Clear any carries from the first line "
         "before you start so they do not get reused.</p>"),
        ("Add the two lines",
         "<p>Standard column addition. The sum of the partial products is the answer.</p>"),
        ("Estimate to check",
         "<p>384 \u00d7 27 is roughly 400 \u00d7 30 = 12,000. An answer near 10,000 is believable; "
         "1,037 or 103,680 is not.</p>"),
    ],
    examples=[
        ("384 \u00d7 27",
         ["7 \u00d7 384: 7\u00d74 = 28 (write 8 carry 2), 7\u00d78 = 56 + 2 = 58 (write 8 carry 5), 7\u00d73 = 21 + 5 = 26. First line: 2,688.",
          "Placeholder zero in the ones column of line two.",
          "2 \u00d7 384 = 768, written in front of the zero: 7,680.",
          "2,688 + 7,680."],
         "10,368"),
        ("56 \u00d7 43",
         ["3 \u00d7 56 = 168.",
          "Placeholder zero, then 4 \u00d7 56 = 224, giving 2,240.",
          "168 + 2,240."],
         "2,408"),
        ("4.2 \u00d7 36",
         ["Ignore the decimal point and work out 42 \u00d7 36.",
          "6 \u00d7 42 = 252. Zero, then 3 \u00d7 42 = 126 \u2192 1,260.",
          "252 + 1,260 = 1,512.",
          "The question had one decimal place in total, so the answer needs one."],
         "151.2"),
    ],
    mistakes=[
        ("Missing the placeholder zero, so the second line is ten times too small.",
         "Write the zero <em>before</em> you start the second multiplication, as a separate deliberate step. It is the single biggest source of lost marks."),
        ("Carrying digits from the first line into the second.",
         "Cross out or erase the first line's carries before starting line two \u2014 or write them above the top number and clear them each time."),
        ("Drifting columns so the final addition is misaligned.",
         "Squared paper, one digit per square. Alignment errors look like multiplication errors but are not."),
        ("Forgetting the decimal point in the answer.",
         "Count the decimal places in the question and put the same number in the answer. 4.2 \u00d7 36 has one, so the answer has one."),
    ],
    sections=[
        ("The grid method, and when to drop it",
         """<p>The grid method splits both numbers by place value into a rectangle of partial
         products. For 384 \u00d7 27 that is six multiplications \u2014 300\u00d720, 80\u00d720, 4\u00d720,
         300\u00d77, 80\u00d77, 4\u00d77 \u2014 which are then totalled.</p>
         <p>It is slower but far more transparent, and it shows clearly <em>why</em> the column
         method works. Most schools teach grid first and move to columns in Year 5. If a child is
         making placeholder errors, going back to the grid for a week usually fixes the
         understanding rather than just the habit.</p>"""),
        ("Three-digit multipliers",
         """<p>Same method, one more line. Multiplying by the hundreds digit needs <em>two</em>
         placeholder zeros, because you are multiplying by 300 rather than by 3. The three partial
         products are then added together in one go.</p>
         <p>This is beyond the KS2 curriculum but appears in extension work and in Year 7.</p>"""),
        ("Checking with the inverse",
         """<p>If 384 \u00d7 27 = 10,368, then 10,368 \u00f7 27 should give 384 back. That is a long
         division, so it is not a cheap check \u2014 the estimate is better value. But for a final
         answer that really matters, the inverse is the only check that is genuinely
         independent.</p>"""),
    ],
    faqs=[
        ("Why do you add a zero on the second line?",
         "Because you are multiplying by the tens digit, which means multiplying by 20, 30 and so on \u2014 not by 2 or 3. The zero shifts the partial product into the right columns."),
        ("Is the grid method still allowed in SATs?",
         "Yes. Arithmetic paper questions are marked on the answer, and the reasoning papers accept any valid method. The curriculum names the formal column method as the expectation, though."),
        ("How do I multiply two decimals?",
         "Ignore both decimal points, multiply as whole numbers, then count the total decimal places in the question and place the point so the answer has the same number."),
        ("What is the fastest way to check a long multiplication?",
         "Round and estimate first, before you calculate. If the real answer is nowhere near the estimate, you have a place-value error \u2014 almost always the missing zero."),
    ],
    cta=("Practise long multiplication", "practice.html?year=6&level=medium"),
    related=["times-tables", "long-division", "multiplying-decimals", "column-addition"],
),

# ---------------------------------------------------------------- 5
dict(
    slug="short-division", cat=CAT, nav="Short division", read=5,
    h1="Short division (the bus stop method)",
    card="Divide by a single digit, carry the remainder, and finish into decimals if you need to.",
    years="Years 4\u20136",
    seo="Short division explained \u2014 the bus stop method step by step | Math It!",
    desc="How to do short division with the bus stop method: dividing digit by digit, carrying remainders, handling a leading digit that is too small, and continuing past the decimal point.",
    keywords="short division, bus stop method, dividing by single digit, short division remainders, KS2 division method, year 5 short division",
    intro="""<p>Short division \u2014 the \u201cbus stop\u201d \u2014 is the method for dividing by a
      single digit. You work left to right, one digit at a time, carrying whatever is left over into
      the next digit.</p>
      <p>It is quicker than long division and children use it far more often. It also underpins
      converting fractions to decimals and simplifying, so it is worth getting fluent.</p>""",
    steps=[
        ("Draw the bus stop",
         "<p>The number being divided goes inside, the divisor outside on the left, and the answer "
         "is built on the roof above \u2014 one digit directly above each digit inside.</p>"),
        ("Divide the first digit",
         "<p>How many times does the divisor go into it? Write that above. Anything left over is "
         "carried as a small digit in front of the next number inside.</p>"),
        ("Carry the remainder and move right",
         "<p>The carried remainder joins the next digit to make a new two-digit number. Divide that, "
         "write the answer above, carry again.</p>"),
        ("Handle a first digit that is too small",
         "<p>If the divisor does not fit, write 0 above that digit and carry the whole digit "
         "forward. 128 \u00f7 4 starts with 4 into 1, which is 0 remainder 1, then 4 into 12.</p>"),
        ("Decide what to do with the final remainder",
         "<p>Three options: leave it as \u201cr 2\u201d, write it as a fraction over the divisor, or "
         "add a decimal point and zeros and keep going. The question will usually tell you.</p>"),
    ],
    examples=[
        ("4,728 \u00f7 6",
         ["6 into 4 doesn't go: write 0, carry the 4.",
          "6 into 47 goes 7 times (42), remainder 5. Write 7, carry 5.",
          "6 into 52 goes 8 times (48), remainder 4. Write 8, carry 4.",
          "6 into 48 goes 8 exactly. Write 8."],
         "788"),
        ("947 \u00f7 4, with a remainder",
         ["4 into 9 goes 2 (8), remainder 1. Write 2, carry 1.",
          "4 into 14 goes 3 (12), remainder 2. Write 3, carry 2.",
          "4 into 27 goes 6 (24), remainder 3."],
         "236 r 3"),
        ("947 \u00f7 4 as a decimal",
         ["Carry on from 236 remainder 3.",
          "Put a decimal point in the answer and write 947.0 inside.",
          "4 into 30 goes 7 (28), remainder 2. Write .7, carry 2.",
          "4 into 20 goes 5 exactly."],
         "236.75"),
        ("3 \u00f7 8 as a decimal",
         ["8 into 3 doesn't go: write 0, add a decimal point, carry the 3.",
          "8 into 30 goes 3 (24), remainder 6.",
          "8 into 60 goes 7 (56), remainder 4.",
          "8 into 40 goes 5 exactly."],
         "0.375"),
    ],
    mistakes=[
        ("Writing the carried remainder as a separate answer digit.",
         "The remainder goes <em>inside</em> the bus stop, as a small digit in front of the next number \u2014 never on the roof."),
        ("Skipping the leading zero when the divisor doesn't fit the first digit.",
         "128 \u00f7 4 must start 0, then 3, then 2 \u2014 and the leading zero is then dropped from the written answer. Omitting it in the working shifts every digit."),
        ("Lining the answer digits up anywhere other than directly above.",
         "One answer digit sits above each digit inside. If they drift, the place value of the answer is wrong."),
        ("Stopping at \u2018r 3\u2019 when the question asked for a decimal.",
         "Read the question. \u2018Give your answer to 2 decimal places\u2019 means adding a point and zeros and continuing."),
    ],
    sections=[
        ("Short or long?",
         """<p>Short division is for single-digit divisors \u2014 anything from 2 to 9, and 11 or 12
         if the child is confident. Two-digit divisors generally need
         <a href="long-division.html" class="link">long division</a>, where the subtraction is
         written out in full because it is too much to hold in your head.</p>
         <p>Some children cope with 12 or 15 in a bus stop. There is no rule against it; the test is
         simply whether they can do the mental subtraction reliably.</p>"""),
        ("Remainders in context",
         """<p>Word problems decide what the remainder means, and the maths alone cannot tell you.
         \u201c47 children, 6 per minibus\u201d gives 7 remainder 5, but you need
         <strong>8</strong> minibuses. \u201c47 cakes shared between 6\u201d gives 7 each with 5 left
         over, and the answer is 7. \u201c\u00a347 split 6 ways\u201d gives \u00a37.83.</p>
         <p>Always re-read the question after dividing. Rounding the wrong way on a remainder
         question is one of the most common SATs reasoning errors.</p>"""),
        ("Fractions to decimals",
         """<p>Any fraction is a division: 3/8 means 3 \u00f7 8. Short division turns it into 0.375.
         This is how children convert fractions that are not in the standard list, and it is why
         fluency here pays off in the fractions topics later.</p>"""),
    ],
    faqs=[
        ("Why is it called the bus stop method?",
         "Because the layout looks like a bus shelter \u2014 a vertical line and a roof over the number being divided. It has no mathematical significance."),
        ("Can I use short division for two-digit divisors?",
         "You can if you can do the mental arithmetic, but most children are more accurate with long division once the divisor is above 12."),
        ("How do I write the remainder as a fraction?",
         "Put the remainder over the divisor. 947 \u00f7 4 = 236 r 3 becomes 236 and three quarters."),
        ("What if the division never ends?",
         "Some do not \u2014 1 \u00f7 3 = 0.333\u2026 recurring. Round to the number of decimal places the question asks for, or leave it as a fraction."),
    ],
    cta=("Practise short division", "practice.html?year=5&level=medium"),
    related=["long-division", "times-tables", "fractions-decimals-percentages", "multiplying-decimals"],
),

# ---------------------------------------------------------------- 6
dict(
    slug="long-division", cat=CAT, nav="Long division", read=8,
    h1="Long division, step by step",
    card="Divide by two digits using DMSB, with a multiples list that removes the guesswork.",
    years="Year 6",
    seo="Long division explained \u2014 the DMSB method with worked examples | Math It!",
    desc="Long division for two-digit divisors, taught through the DMSB cycle: divide, multiply, subtract, bring down. Includes building a multiples list, handling remainders and checking your answer.",
    keywords="long division, long division method, DMSB, dividing by two digit numbers, long division steps, year 6 long division, KS2 long division",
    intro="""<p>Long division is the method for dividing by a two-digit number. It looks intimidating
      because the page fills up, but it is only four steps on a loop: <strong>divide, multiply,
      subtract, bring down</strong> \u2014 DMSB.</p>
      <p>The step that actually causes trouble is the first one: deciding how many times 23 goes into
      187. The fix is to stop guessing and write out a multiples list before you begin.</p>""",
    steps=[
        ("Write out the multiples first",
         "<p>Before any division, list the divisor \u00d7 1 up to \u00d7 9 down the side of the page. "
         "For 23: 23, 46, 69, 92, 115, 138, 161, 184, 207. This takes thirty seconds and removes "
         "every guess from the rest of the calculation.</p>"),
        ("D \u2014 Divide",
         "<p>Look at the leading digits of the dividend and find the largest multiple on your list "
         "that fits. Write how many times it goes above the line, directly above the last digit you "
         "used.</p>"),
        ("M \u2014 Multiply",
         "<p>Multiply the divisor by that answer digit and write the product underneath, lined up "
         "with the digits you divided into. You already have it on your list.</p>"),
        ("S \u2014 Subtract",
         "<p>Subtract to find what is left. The result must be smaller than the divisor \u2014 if it "
         "is not, your answer digit was too small, so go back and increase it.</p>"),
        ("B \u2014 Bring down",
         "<p>Bring the next digit of the dividend down next to the remainder, making a new number. "
         "Then loop back to Divide.</p>"),
        ("Stop, or continue into decimals",
         "<p>When there are no digits left to bring down, whatever remains is the remainder. For a "
         "decimal answer, add a decimal point and zeros to the dividend and keep going.</p>"),
    ],
    examples=[
        ("4,312 \u00f7 23",
         ["Multiples of 23: 23, 46, 69, 92, 115, 138, 161, 184, 207.",
          "23 into 43 \u2192 1 (23). Subtract: 43 \u2212 23 = 20. Bring down 1 \u2192 201.",
          "23 into 201 \u2192 8 (184). Subtract: 201 \u2212 184 = 17. Bring down 2 \u2192 172.",
          "23 into 172 \u2192 7 (161). Subtract: 172 \u2212 161 = 11. Nothing left to bring down.",
          "Answer digits so far: 1, 8, 7, remainder 11."],
         "187 r 11"),
        ("4,312 \u00f7 23 to 1 decimal place",
         ["Continue from 187 remainder 11.",
          "Add a decimal point to the answer and write 4,312.0 inside.",
          "Bring down the 0 \u2192 110. 23 into 110 \u2192 4 (92). Remainder 18.",
          "Next digit would be 7, so 187.4 is already correct to 1 d.p."],
         "187.4"),
        ("952 \u00f7 17",
         ["Multiples of 17: 17, 34, 51, 68, 85, 102, 119, 136, 153.",
          "17 into 95 \u2192 5 (85). Subtract: 10. Bring down 2 \u2192 102.",
          "17 into 102 \u2192 6 exactly (102). Subtract: 0.",
          "No remainder."],
         "56"),
    ],
    mistakes=[
        ("Guessing the answer digit and discovering the subtraction goes negative.",
         "Write the multiples list first. With 23, 46, 69\u2026 in front of you there is nothing left to guess."),
        ("Leaving a remainder that is larger than the divisor.",
         "That always means the answer digit was one too small. Increase it by 1 and redo that subtraction."),
        ("Forgetting to write a 0 above when the divisor doesn't fit.",
         "Every digit brought down must produce an answer digit, even if it is 0. Skipping it shifts the whole answer."),
        ("Letting the columns drift so subtractions misalign.",
         "Use squared paper and keep one digit per square. Long division is as much a layout skill as an arithmetic one."),
    ],
    sections=[
        ("Chunking \u2014 the safety net",
         """<p>If formal long division will not stick, chunking gets the same answer with less
         precision required. Subtract easy multiples of the divisor repeatedly and keep a tally:</p>
         <p class="font-mono">4,312 \u2212 2,300 (100 \u00d7 23) = 2,012<br>
         2,012 \u2212 1,840 (80 \u00d7 23) = 172<br>
         172 \u2212 161 (7 \u00d7 23) = 11<br>
         100 + 80 + 7 = 187, remainder 11</p>
         <p>It is slower and uses more paper, but it is almost impossible to get badly wrong, and it
         makes the formal method's logic obvious. Plenty of children use chunking in Year 6 SATs and
         score full marks.</p>"""),
        ("Remainders: three valid answers",
         """<p>4,312 \u00f7 23 can correctly be written as <strong>187 r 11</strong>,
         <strong>187 and 11/23</strong>, or <strong>187.478\u2026</strong> to however many decimal
         places are asked for. All three are the same number expressed differently.</p>
         <p>Read the question: \u201cgive your answer as a mixed number\u201d, \u201cto 2 decimal
         places\u201d and \u201chow many full boxes\u201d all want different things from the same
         division.</p>"""),
        ("Checking the answer",
         """<p>Multiply back and add the remainder: 187 \u00d7 23 = 4,301, plus 11 gives 4,312. That is
         a complete, independent check and it is worth the minute it takes on a multi-mark
         question.</p>
         <p>Estimate first too: 4,312 \u00f7 23 is roughly 4,000 \u00f7 20 = 200, so an answer of 187 is
         sensible and an answer of 18.7 or 1,870 is not.</p>"""),
        ("Why it is worth the effort",
         """<p>Long division is the last and hardest of the four formal written methods, and it is
         the one adults most often say they never use. That is partly true \u2014 but the skill it
         builds, holding a multi-step procedure accurately while tracking place value, is exactly
         what algebra demands two years later. Children who can do long division tend to cope with
         algebraic long division and with multi-step problems generally.</p>"""),
    ],
    faqs=[
        ("What does DMSB stand for?",
         "Divide, Multiply, Subtract, Bring down \u2014 the four steps that repeat until the division is finished."),
        ("Is chunking acceptable in SATs?",
         "Yes. The arithmetic paper marks the answer, and reasoning papers accept any valid method. Long division is the curriculum expectation, but chunking that produces the right answer scores the same."),
        ("How do I know how many times the divisor goes in?",
         "Write out multiples of the divisor from \u00d71 to \u00d79 before starting. Then you are reading from a list, not guessing."),
        ("What if the remainder is bigger than the divisor?",
         "Your answer digit was too small. Go back one step, increase it by one, and redo the subtraction."),
        ("When do children learn long division?",
         "Year 6 in England. Dividing a four-digit number by a two-digit number using the formal method is an explicit Year 6 objective."),
    ],
    cta=("Practise long division", "practice.html?year=6&level=hard"),
    related=["short-division", "long-multiplication", "times-tables", "order-of-operations"],
),

# ---------------------------------------------------------------- 7
dict(
    slug="order-of-operations", cat=CAT, nav="Order of operations (BIDMAS)", read=6,
    h1="Order of operations: BIDMAS without the myths",
    card="Why division and multiplication rank equally, and what to do when they both appear.",
    years="Years 5\u20136",
    seo="BIDMAS explained \u2014 order of operations without the myths | Math It!",
    desc="BIDMAS properly explained: brackets, indices, then division and multiplication together, then addition and subtraction together. The two myths that cause most errors, with worked examples.",
    keywords="BIDMAS, order of operations, BODMAS, PEMDAS, BIDMAS rules, maths order of operations, year 6 BIDMAS, KS2 order of operations",
    intro="""<p>BIDMAS tells you which operation to carry out first when a calculation has several.
      It stands for <strong>B</strong>rackets, <strong>I</strong>ndices,
      <strong>D</strong>ivision and <strong>M</strong>ultiplication,
      <strong>A</strong>ddition and <strong>S</strong>ubtraction.</p>
      <p>The acronym is useful and slightly misleading at the same time. It is read as six separate
      ranks, when really there are only four \u2014 and that misreading is the cause of almost every
      BIDMAS error.</p>""",
    steps=[
        ("Brackets first",
         "<p>Work out everything inside brackets before anything else. If brackets are nested, do "
         "the innermost pair first.</p>"),
        ("Then indices",
         "<p>Squares, cubes and roots. 3 + 4\u00b2 means 3 + 16 = 19, not 7\u00b2.</p>"),
        ("Then division and multiplication together, left to right",
         "<p>These share one rank. Neither beats the other \u2014 you do whichever comes first "
         "reading left to right.</p>"),
        ("Then addition and subtraction together, left to right",
         "<p>Also one shared rank. Again, left to right decides.</p>"),
        ("Rewrite as you go",
         "<p>Write the whole calculation out again at each stage rather than scribbling over it. "
         "Most BIDMAS errors are transcription errors, not logic errors.</p>"),
    ],
    examples=[
        ("20 \u2212 3 \u00d7 4",
         ["Multiplication outranks subtraction.",
          "3 \u00d7 4 = 12.",
          "Rewrite: 20 \u2212 12."],
         "8"),
        ("24 \u00f7 6 \u00d7 2",
         ["Division and multiplication share a rank, so work left to right.",
          "24 \u00f7 6 = 4.",
          "4 \u00d7 2 = 8. (Doing the multiplication first would give the wrong answer, 2.)"],
         "8"),
        ("10 \u2212 4 + 3",
         ["Addition and subtraction share a rank \u2014 left to right.",
          "10 \u2212 4 = 6.",
          "6 + 3 = 9. (Doing the addition first would give 3.)"],
         "9"),
        ("2 \u00d7 (3 + 4)\u00b2",
         ["Brackets first: 3 + 4 = 7.",
          "Indices next: 7\u00b2 = 49.",
          "Then multiply: 2 \u00d7 49."],
         "98"),
        ("48 \u00f7 (2 \u00d7 3) + 5\u00b2",
         ["Brackets: 2 \u00d7 3 = 6.",
          "Indices: 5\u00b2 = 25.",
          "Division: 48 \u00f7 6 = 8.",
          "Addition: 8 + 25."],
         "33"),
    ],
    mistakes=[
        ("Thinking division always comes before multiplication because D is before M.",
         "They share one rank. 24 \u00f7 6 \u00d7 2 is done left to right and equals 8, not 2."),
        ("Thinking addition always comes before subtraction.",
         "Also one shared rank. 10 \u2212 4 + 3 is done left to right and equals 9, not 3."),
        ("Reading 3 + 4\u00b2 as 7\u00b2.",
         "Indices bind tightly to the number immediately before them. Only the 4 is squared, so it is 3 + 16."),
        ("Ignoring an implied bracket in a fraction.",
         "A fraction bar acts as a bracket on both top and bottom. (12 + 8) \u00f7 (2 + 3) must be worked as 20 \u00f7 5, not 12 + 4 + 3."),
    ],
    sections=[
        ("BIDMAS, BODMAS, PEMDAS \u2014 same thing",
         """<p>BODMAS uses \u201cOrders\u201d for what BIDMAS calls \u201cIndices\u201d. The American
         PEMDAS uses \u201cParentheses\u201d and \u201cExponents\u201d. All three describe exactly the
         same hierarchy; only the vocabulary differs.</p>
         <p>If your child's school uses one and a website uses another, nothing is wrong \u2014 but
         pick one and stay with it at home to avoid confusion.</p>"""),
        ("The four ranks, honestly stated",
         """<p>It is genuinely four levels, not six:</p>
         <ol>
           <li>Brackets</li>
           <li>Indices</li>
           <li>Division <em>and</em> multiplication, left to right</li>
           <li>Addition <em>and</em> subtraction, left to right</li>
         </ol>
         <p>Teaching it this way from the start prevents both of the big myths. Some schools now
         write it as B I DM AS with the pairs grouped, which is clearer.</p>"""),
        ("Brackets you cannot see",
         """<p>Several notations contain invisible brackets:</p>
         <ul>
           <li>A fraction bar: the whole numerator and the whole denominator are each bracketed.</li>
           <li>A square root sign: everything under the bar is bracketed.</li>
           <li>A negative sign in front of a bracket: \u22122(3 + 4) means \u22122 \u00d7 7.</li>
         </ul>
         <p>Where there is doubt, add the brackets yourself. Nobody has ever lost a mark for
         clarifying a calculation.</p>"""),
        ("Why the convention exists",
         """<p>The order is not a law of nature, it is an agreement \u2014 but a necessary one. Without
         it, 2 + 3 \u00d7 4 could be 20 or 14 and every formula would need brackets everywhere. The
         specific choice gives multiplication priority because it is repeated addition, so 2 + 3 + 3
         + 3 + 3 and 2 + 3 \u00d7 4 come out the same. That consistency is what makes algebra
         writable.</p>"""),
    ],
    faqs=[
        ("Is it BIDMAS or BODMAS?",
         "Both, and they mean the same. BIDMAS says Indices, BODMAS says Orders. UK schools are split roughly evenly."),
        ("Does multiplication really not come before division?",
         "Correct \u2014 they are equal in rank and you work left to right. This is the most commonly taught mistake in the whole topic."),
        ("What about those viral Facebook puzzles?",
         "They are almost always ambiguous notation, usually an implied multiplication like 6 \u00f7 2(1+2). Mathematicians would simply add brackets. They are not a test of BIDMAS, they are a test of bad typography."),
        ("When is BIDMAS taught?",
         "Year 6 in England, where children are expected to use their knowledge of the order of operations to carry out calculations involving the four operations."),
    ],
    cta=("Practise BIDMAS questions", "practice.html?year=6&level=hard"),
    related=["square-cube-numbers", "simple-algebra", "long-multiplication", "mental-strategies"],
),

]
