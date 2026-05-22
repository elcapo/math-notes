## 00:00

Welcome back to an introduction to real
analysis. We're now in chapter 5,
section one, the remon integral,
specifically remon and darbo integrals.
Now, an integral is going to be a way to
sum up the values of a function. It's
worth stating that students, especially
those who have only taken an elementary
calculus course, are often confused
about what the difference is between an
integral and an anti-derivative, or if
there even is a difference. Now the
integral informally for us is simply the
area under the curve of a function and
not anything else. The fact that we may
find an anti-derivative by using an
integral and vice versa is a very
non-trivial result we're going to have
to prove.
We will be defining the remon integral
but actually using the Darabau integral.
Uh these definitions are equivalent.
There are several exercises to
illustrate that, but the Darbo integral
is a technically simpler definition that
lends itself better to the sorts of
proofs we're going to be constructing.

## 00:01

So, we need to integrate a bounded
function defined on an interval from A
to B, including its end points. We're
going to define two auxiliary integrals
that will be defined no matter what for
any bounded function. Only after
defining these two things can we talk
about the remon integral and the
functions which it can integrate. The
so-called remon integraable functions.
So first let's define a partition. A
partition of the interval from a to b is
a finite set x knot through xn which are
strictly increasing beginning at a and
ending at b. So you select a finite
collection of points. You have to pick
the left end point a. You have to pick
the right end point B and you can pick
some quantity in between and you order
them from left to right.
Then we will denote delta x i as x i - x
i -1. This is simply the length of the i
interval or the i piece of the

## 00:02

Now suppose you have a function with
domain the interval from a to b
including its end points. Suppose that
function is bounded and you have a
partition. Denote little m subi to be
the infom of f ofx on the interval from
x i minus one to x i including the end
points and capital m i to be the supreum
of f ofx on that same interval. This is
notation we will be very consistently
using through this chapter. Capital p is
a partition. The points in it are x
subi. Big m subi and little m subi are
the soup and int respectively of the
function on the intervals created by the
So now we have a function f. Domain is
the interval from a to b including the
end points. It is bounded that is a
running assumption and p is a partition
with little m and big m i defined as
previously done. Then we let capital l
of the partition and the function to be
the sum as i runs from 1 to n. In other
words, over each interval of the

## 00:03

partition of little mi * delta xi, the
in of the function on a particular
interval times the length of that
interval. And capital U of p comma f is
the sum over the pieces of the partition
indexed from 1 to n. Capital mi * delta
xi, the soup of the function on a
particular interval times the length of
that interval.
We call these the lower and upper darau
sums of the function with respect to the
partition P. So the function f is fixed
but you need to specify a partition in
order to talk about the lower and upper
sums of that partition.
Now the geometric idea of darau sums is
indicated right here. The lower sum is
the area of the shaded rectangles.
Having made a partition of x knot
through x8. On each interval, we can
make a rectangle. The width is delta xi,
the width of each interval.

## 00:04

The height of the rectangles for the
lower sum is given by the little m's,
the in of the function. Whereas the
upper sum is given by the capital m or
the soup. Now this picture is a
continuous curve meaning in and soup are
actually min and max. But in general
think of it as in and soup.
So the width again given by delta xi.
Also note these delta xis do not have to
all be equal to each other. In this
picture it appears that all of the
intervals are of equal width. That is
not a requirement. It's just a
convenience when drawing pictures.
So we move on to proposition 5.1.2.
Suppose you have one of these functions
f. It's a bounded function. Its domain
is an interval including the end points.
Also assume that you have a lowerbound
little m and an upperbound capital m.
Then regardless of the partition,
the lower sum is always less than or
equal to the upper sum. That's this
inner inequality. However, the lower sum

## 00:05

cannot be less than the overall
lower bound little m times the width of
the overall interval and the upper sum
cannot be larger than the overall upper
bound capital m times the width of the
The proof of
this partition is actually fairly
straightforward, but it will be very
useful for us. So suppose you have an
arbitrary partition P. We're going to
denote it as the points x knot through
xn. Then if you add up just delta x i,
forget any little m's or big m's. Delta
x i is simply x i - x i -1. But we end
up with what is called a telescoping
sum. When i equals 1, we get a plus x1.
But when I equals 2, we get a minus x1,
which will cancel out this one right
here. So various terms in this sum will
cancel out. And the only thing that
remains is the final plus xn and the

## 00:06

first minus x knot. But remember for any
partition the last term xn must be the
right end point b and the first term x
knot must be the left end point a. So
regardless of the partition if you sum
up the delta x i's you recover the
length of the interval b minus a.
Then for each index I
because the i interval is a subset of
the overall interval the set of values
taken on that interval is a subset of
the set of values taken overall.
Therefore the in on a particular
interval is bigger than or equal to a
global lower bound and the soup on a
particular interval is less than or
equal to any particular global upper
So we have established that if you add
up the delta x i's you recover b minus
a. Every in on a particular interval is
bigger than or equal to whatever lower

## 00:07

bound was established here in the setup
of the proposition. And any particular
soup is less than or equal to whatever
this upper bound is. Then we simply
establish this long chain of
inequalities. The overall m * b minus a.
B minus a can be represented as this
sum. This is now a constant. as far as
the sum is concerned and can be factored
in. But every little m is less than or
equal to any particular uh little m
M subi is the in on a particular
interval is always less than or equal to
capital m subi the soup on a particular
interval. However, each capital m subi
is less than or equal to this capital m
which is a constant which may be
factored out. So overall we have little
m * b minus a less than or equal to the
lower sum less than or equal to the
upper sum less than or equal to capital
m * b minus a.
Okay. And those interior terms again are
exactly the lower and upper sums which
completes the proof of the proposition.

## 00:08

So what's really the purpose of this
proposition which was honestly fairly
straightforward to prove. Consider the
function in the interval to be fixed and
let script P be a set of all possible
partitions of the interval. So all
finite subsets of the interval which
have to include the left and right
endpoint. Now we can sort of construct
these abstract functions L and U to be
the lower and upper sum of each
particular partition.
We've just established that these
functions are bounded. No matter what
the proposition, the lower and upper
sums are always bounded below and above
by these fixed constants. So no matter
what partition you create, you have this
global lower bound and upper bound for
whatever the lower and upper sums could
possibly be.
So therefore the range of this lower

## 00:09

bound function and upper bound function
which maps a partition to the lower and
upper bound of that partition. These
functions are bounded and therefore have
an inf and a soup.
Now one choice of each of these is more
interesting than the other.
So we move on to our first real
definition regarding integrability.
Definition 5.1.3.
Suppose you have this bounded function
on the interval from A to B including
the end points. Script P denotes all
possible partitions. We can define
the integral from A to B with a big line
over it f ofx dx to be the infom of all
possible upper sums. Similarly, the
integral from a to b of f ofx dx with a
line under it to be the supreum of all
possible lower sums. These are referred
to as the upper and lower darbo
integrals of the function f. Note they
always exist for any function f which is

## 00:10

bounded on this interval. All upper and
lower sums are bounded above and below.
Meaning the upper sums have an infom
sums have a supreum. So the existence of
these things is not in question provided
the function f was bounded to begin
Now the dx that we wrote before will
probably not have raised any eyebrows
but it's also not necessary. We haven't
defined what it is or what it means and
for this material it is actually
irrelevant and you can ignore it. So
actually we're generally just going to
write this for the upper integral of f
on the interval from a to b and this for
the lower integral of f. the ofx dx is
uh at best not necessary.
Now if integration is going to be a
reasonable concept that we want to talk
about we would hope that these two
quantities would be equal and if they
are we would call that the integral

## 00:11

but these quantities the upper and lower
darbo integral are not always the same
thing. So let's see an example. Let f be
the dearishlay function. One of our
classic function that does bad things.
This is the function that is one when
the input is rational and zero when the
input is irrational. Then for any
interval from a to b we have the upper
integral is b minus a while the lower
integral is zero.
The proof is pretty short. Now for any
partition for any interval in that
partition that interval will contain
both rational and irrational numbers. It
is worth pointing out that our
definition of partition required these x
sub iis to be strictly increasing. So
this interval does contain uncountably
many points from the left to the right.
It contains both rational and irrational
numbers. So regardless of the partition
and regardless of index i, the in on
that interval is zero and the soup is

## 00:12

So for any partition, the upper sum may
be computed as 1 times the length of the
interval. But as previously discussed,
when you sum up the lengths of the
pieces of the partition, you recover the
length of the interval overall. While
the lower sum is simply the sum of 0 *
delta xi, which will just be zero. So
the upper and lower sums are constant.
Every upper sum you could ever take is
equal to b minus a and every lower sum
you could possibly take is zero. So it
is quite trivial to take the in and soup
over upper and lower sums respectively.
The in over all upper sums is b minus a
because every upper sum is b minus a and
the soup over all lower sums is zero
because every lower sum is zero. So we
have here an example of a function where
the upper and lower darbo integrals will
not take the same value.
Now we have defined all previous terms

## 00:13

for a function f defined on a fixed
interval from a to b. Now if f is
defined on a larger set for example all
real numbers then for any particular
interval from a to b we can apply all
the same definitions. What is important
is that the function f be bounded on
each interval but not necessarily on its
entire domain. We only required
functions to be bounded on the interval
where we are trying to define these
things. For example, f ofx= x is not
technically a bounded function but on
any particular interval you could pick
it is. So we have no problem writing
something like this. Our definitions
only allow us to write an upper integral
if this function is bounded. f ofx= x is
not bounded on its entire domain. But if
we restrict ourselves to going just from
a to b, it certainly is.
Now, one very important tool in
determining which functions will have
the upper and lower darbo integral equal

## 00:14

to each other is going to be to consider
what happens when we modify an existing
partition by adding some points to it.
So we refer to adding points to a
partition as making the partition finer.
This leads us to the following
definition, a refinement. Let P and P
tilda both be partitions of the same
interval from A to B. If P is a subset
of P tilda, we say that P tilda is a
refinement of P. Given two partitions P1
and P2, which may not be refinements of
one another. If we simply take the union
of both of them, well then P1 and P2 are
both subsets of this union. So we call
it the mutual refinement of P1 and P2.
This partition here, it is a partition.
It includes the left end point and the
right endpoint and a finite collection
of points in between. Because it
contains each of these, we can say it is

## 00:15

a refinement of P1. It is also a
refinement of P2. Hence the term mutual
Note that tilda p is a refinement of p
provided p is a subset of tilda p. This
was the definition. So tilda p contains
every point that p had plus possibly
more. That's why p1 union p2 is
automatically a refinement of both and
in fact can be defined as the smallest
set that is a refinement of both. Now
it's important here that the interval
from A to B is fixed and not changing.
If you change the interval between two
different partitions, none of this
really makes any sense. So for example,
here is a partition of the interval from
0 to 1 0 a/4 6 1. If we also add in 28.9
and.99, but we still also have 0 a/4 6
and 1, we've made a refinement. We had a

## 00:16

partition and we added some points to
So proposition 5.1.7 is really going to
get to the heart of what we're going to
be using refinements for. Suppose you
have a function the running assumption
being it's bounded on an interval from A
to B including the end points. P and P
tilda are two partitions where P tilda
is a refinement of P. Then what do we
The lower sum of P is less than or equal
to the lower sum of its refinement P
tilda. Similarly, the upper sum of P is
greater than or equal to the upper sum
of its refinement P tilda.
Now, as
far as proving this goes, it's worth
pointing out there is a middle
inequality stated here that the lower
sum of P tilda is less than or equal to
the upper sum of P tilda. We already
covered this in an earlier proposition.
For one partition that isn't changing,
the lower sum is always less than or
equal to the upper sum. Now since
partitions have to be finite, P tilda

## 00:17

contains all points of P plus finitely
many more points. So if we can establish
the outer inequalities when we simply
add one point to P, then by repeating
this finitely many times, we could
obtain the result we wanted. Okay, if by
adding a single point, you always get
inequalities moving in the direction you
want, you can simply add one point, then
another then another, and get to the end
result. Similarly for the upper sums. So
we are simply going to assume without
loss of generality that P tilda is a
refinement made by simply adding a
single point which we're going to call
Now since P tilda is obtained by adding
a single point to P. If Y was one of the
original points of P, there's nothing to
prove. P and P tilda are equal as sets.
So their lower and upper sums are equal.
So now let's assume that y is not an
element of the original partition in
which case there is a unique index k so
that y is strictly in between x k minus1

## 00:18

and x k.
So here is the partition p that we
started with x knot through xn and p
tilda has all of the same elements but
in between these two elements we've
inserted a new one y.
Now if I is less than or equal to K
minus one or if I is bigger than or
equal to K + one the interval in the
original partition appears exactly the
same in the new one. So the soup on this
interval will be the soup on this one
and so forth.
So specifically if we take the
difference L the lower sum of the
refinement minus the lower sum of the
original all terms will cancel except in
the original partition the interval from
xkus1 to x k does not appear down here
and in the refinement these two
intervals do not appear in the partition
above. So if we compute the lower sum of
p tilda minus the lower sum of p,

## 00:19

everything cancels except for the pieces
of the partition in between x k minus
one and x k.
So here are our two partitions p and p
tilda. We just want to see what's going
on in between x k minus one and x k. Now
in the original partition P, we don't
need to change any notation because our
notation is built around that partition.
What we do need to change for P tilda
however has to do with our choice of
index. So the first interval goes from 0
to 1. The second interval from 1 to 2.
But now the kith interval goes from k
minus one to y. The k + first interval
goes from y to x k. Now the k + 2
interval goes from x k to x k + one. And
now our indices are just off by one. So
we're going to denote mtilda subk
to be the in on this interval from x k
minus1 to y and m tilda k +1 to be the

## 00:20

in from y to x k.
Now m tilda is at least as large as mk
but so is m tilda k + one because this
interval and that one x k minus one to y
and y to x k are both subsets of x kus1
to x k. So the values taken by f on each
of these smaller intervals are subsets
of the values taken by f on the large
interval. And if you pass to a subset
your inf can only go up. So the inf on
the left piece and the inf on the right
piece are both bigger than or equal to
the overall inf.
So here are our two partitions. Here are
our ins on the two pieces of the
refinement that don't cancel out when we
take a difference. And here's sort of
the picture. Okay, from x k minus one to
x k we have broken this up into two
pieces. This blue dotted line is the

## 00:21

overall inf. on one piece the inf will
actually be equal and on the other it
can only go up.
Okay, so both ins are bigger than or
equal to the in we started with.
So if both ins on these two small new
created pieces in the partition are
bigger than or equal to the in the
original partition. If we take this
difference again all terms cancel except
those that involve between x k minus1
and x k. So the only terms that survive
in taking the difference are these two
pieces from the lower sum of the
refinement minus just this piece from
the lower sum of the original.
But now m tilda k and m tilda k + one
are bigger than or equal to mk. So
replace all of these with mks in which
case this mk may be factored out and you
get a y which cancels this minus y a
minus x k minus one which cancels this
plus x k -1 and an xk which cancels this

## 00:22

minus x k. So the dis the difference of
the lower sum of the refinement minus
the lower sum of the original is bigger
than or equal to zero. That's exactly
the claim on the left here.
And there is an exercise that covers
this inequality on the right. It's
essentially the same argument. Some
inequalities merely get reversed.
Moving on to prop 5.1.8. Again, our same
assumptions. F is a function bounded on
the interval from a to b. If it's
bounded, we're just going to pick a
little m and a big m to be a global
lower and upper bound respectively. Then
global lower bound time length of
interval less than or equal to lower
integral less than or equal to upper
integral less than or equal to global
upper bound time length of interval.
Proof pretty straightforward for any
partition P. We have already established
that we have this chain of inequalities
where our left and right uh terms on

## 00:23

this chain of inequalities are exactly
what we want to have. Now just look at
lower sums. We have little m * b minus a
is less than or equal to every
particular lower sum. So the lower
integral is the soup of all lower sums.
So it has to be an upper bound on the
lower sums.
Any particular upper bound on the set of
lower sums must be bigger than or equal
to this particular lower bound on the
set of lower sums. Therefore,
the lower integral, the soup of the
lower sums and upper bound on the lower
sums is bigger than or equal to little
m* b minus a. And the right is exactly
the same derivation.
Okay, we actually already did the hard
work and hard is you know carrying a lot
of weight here in this chain of
inequalities. Okay, so really you just
take this here and pass to a soup of all
these. Similarly, take this inequality
and pass to an in of all those.

## 00:24

which is to say it's the middle
inequality that's really the point. The
left inequality, the right inequality,
those were pretty straightforward. It's
the middle one. Let P1 and P2 be
arbitrary partitions of the interval
from A to B and let P tilda be their
mutual refinement. Then what we've
already established is that by passing
two refinements,
the lower sum can only go up and the
upper sum can only go down. Note, I have
P1 on the left and P2 on the right. But
since P tilda is a mutual refinement,
I get all of these inequalities. The
middle one just saying the lower sum of
one particular partition less than or
equal to the upper sum.
So for any particular partitions P1 and
P2, we obtain this. The lower sum of P1
is less than or equal to the upper sum
of P2. So now let's think way back to
prop 1.2.7.
If we have non-mpy sets A and B where
every element of A is less than or equal

## 00:25

to every element of B, then the soup of
A is in fact less than or equal to the
inf of B. So what do we have here? Every
lower sum is less than or equal to every
upper sum. So the soup of the lower sums
is less than or equal to the in of the
upper sums. And we obtain that middle
inequality we wanted to complete the
proof of prop 5.1.8.
Now we can finally define the reman
integral. Now the reman integral can
only be defined on a certain class of
functions called the remon integraable
functions. But as previously mentioned,
we're actually using darbo integrals and
darbo integration. The equivalence of
the two notions is developed in the
following three exercises. We're not
focused on the exercises here. Just note
while we keep throwing out the term
remon integral, remon integration, we're
really doing Darbo integration, it
happens to be exactly the same thing
once you do those three exercises.

## 00:26

So here is the definition of the Darbo
integral. Let f be a bounded function on
the interval from a to b. And suppose
the lower integral equals the upper
integral. Then you say the function is
Darbo integraable. And this value the
shared value between the upper and lower
integrals is written as the integral of
f from a to b.
Now by definition any darbo integraable
function has to be bounded because the
notion of upper and lower integral only
existed for bounded functions. Now
because prop 5.1.8 gave us this chain of
inequalities right here where f ofx is
bounded below by m and above by capital
m, we can immediately state the
If you have a bounded function on the
interval from a to b and it's darbo
integral and you have a global lower and
upper bound little m and capital m
respectively then whatever the value of
the integral it has to be in between
the lower bound times the length of the

## 00:27

interval and the upper bound time the
length of the interval.
A slight modification on the previous
proposition. Suppose you have a bounded
function f on the interval from a to b.
Let capital m be an upper bound on the
absolute value of f ofx. Then the
absolute value of the integral is less
than or equal to that capital m times
the length of the interval.
Okay, moving on to an example. Suppose f
ofx is a constant function then we can
in fact set a global lower and upper
bound on the function to be the same
value c. Therefore, by this proposition,
the lower integral is bigger than or
equal to lower bound * length of
interval. The upper integral less than
or equal to upper bound time length of
interval. Since this global lower and
upper bound are the same number, we in
fact get equality throughout. Meaning
that the lower integral is equal to the
upper integral. And therefore, the
function is Darbo integraable. And the
value of the integral must be the

## 00:28

constant times the length of the
So constant functions are integraable.
That's nice, but doesn't tell us very
much. Let's look at another example. F
is defined on the interval from 0 to 2.
So that it goes from a value of 0 to 1
exactly at x= 1. And at this point, you
just choose to be this average value
1/2. We claim the value of the integral
is exactly one. It is integraable first
of all, and the value of the integral is
one. Now let epsilon be arbitrary and
I'm going to make a partition to go from
zero to just shy of one then to just
above one and then all the way to two.
So here is our partition where these
pieces are very very close to one. This
is exactly zero. I I put it slightly to
the right so you can see the green line
and this is at exactly two.
Now on the first interval the function
is constantly zero. So the in and soup

## 00:29

are both zero. On the last interval, the
function is constantly one. So the in
and soup are both one. On this little
piece in the middle, the in is zero and
the soup is one. Note, what's really
important here is that we are not
obligated to make these pieces the same
width. We're very deliberately making
the first piece of our interval and the
third piece take up most of the domain.
the single point at x= 1 where the
function does something non-constant
looking we're isolating in a very small
piece of the partition.
Now we can simply compute the value of
the lower sum and the value of the upper
So we computed the value of the lower
and upper sums for this specific
partition where epsilon was an arbitrary
number and we find that the distance
between the upper and lower sums is
exactly epsilon. These two things when I
take the difference cancel out as do
these. The only thing that doesn't is
that intermediate piece.

## 00:30

for any particular partition the lower
sum is less than or equal to the lower
integral because this was the soup of
all lower sums. Similarly the upper
integral is less than or equal to the
upper sum. Since these two things are
now epsilon apart
and we have the upper and lower
integrals must be in between them and
epsilon was arbitrary. We have that the
distance between these two things is
less than epsilon. For arbitrary
positive number they must be the same
number. The upper and lower integrals
are equal. The function is darbo
Now that we know the function is
integraable, we can ask what is the
value of the integral. Now we already
stated this chain of inequalities.
However, we now know that this interior
inequality is actually an equality. The
function is integraable. For this
particular partition, we computed 1
minus epsilon for the lower sum and 1

## 00:31

plus epsilon for the upper sum. Whatever
the value is, it must be in between
these. And since epsilon was arbitrary,
we're done. The value of the integral
from 0 to two must be exactly one.
Now, in the previous example, we made a
very specific partition so that the
difference between the upper and lower
sums was as small as we wanted an
arbitrary epsilon. Can this technique be
generalized to get a very useful result?
Yes. and it's going to be our main way
of showing that a function can have an
So the following result is more or less
the major reason at least in my mind
that Darbo integraability rather than
remon integring
definition for how we want to put
together proofs because this particular
result takes a lot of groundwork for
remon integ.
So here it is prop 5.1.13.

## 00:32

Again we have a bounded function on the
interval from a to b. Then f is darbo
integraable if and only if for every
positive epsilon we may find one
specific partition p so that the
difference between the upper and lower
sums is less than epsilon.
So how are we going to prove this? If f
is integral
then the upper and lower integrals are
equal to each other. Now let epsilon be
positive. We can pick partitions p1 and
p2 so that we have both of these
inequalities. First because the lower
integral is the soup of the lower sums.
If I take epsilon away from it, I am no
longer an upper bound on the set of
lower sums. Meaning there is one
particular lower sum bigger than this.
Similarly, I can find one particular
upper sum less than or equal to this.
Now I can mutually refine the P1 and P2
we just picked to get in a partition P.

## 00:33

We will see this value less than or
equal to the lower sum of P1 less than
or equal to the lower sum of this mutual
refinement. For the mutual refinement P,
the lower sum is less than or equal to
the upper sum. However, the upper sum of
the refinement is less than or equal to
the upper sum of the thing it came from
P2 which was less than or equal to this
upper integral plus plus epsilon. And
now this lower integral and upper
integral are in fact just the integral.
So now what do we have? The lower sum
and the upper sum for this partition P
are in the same interval.
The value of the integral minus epsilon,
the value of the integral plus epsilon.
So the distance between them is less
than 2 epsilon. And of course since
epsilon was arbitrary, we could have
begun with an epsilon over two.
Now that was half the proof. If the
function is integraable, then we can
find a partition with this property. The
other direction was really the point. We

## 00:34

want to say if I can find one partition
with this property, then the function
must be integraable. Let epsilon be
positive and let p be a partition so
that the difference between the upper
and lower sums for this particular
partition is less than epsilon. As we
saw in a previous example,
the lower sum of this partition less
than or equal to the soup of the lower
sums. The lower integral is always less
than or equal to the upper integral. And
the upper integral is less than or equal
to one particular upper sum specifically
for this partition.
Since the distance between this lower
and upper sum was less than epsilon, so
too the distance between these lower and
upper integrals is less than epsilon.
And again, since epsilon was arbitrary,
the lower integral and upper integral
must be equal. And therefore, by
definition, the function f is darbo
So let's look at a variant on example
We're going to show that f ofx= x is
integraable on any particular interval
from a to b. We will not compute the

## 00:35

value of the integral. That's worth
stressing. The previous result simply
tells us if we can find a partition with
a certain property, the function can
have an integral. But it does not tell
us how to find it. So let epsilon be
positive and let n be very very large so
that whatever b and a are b minus a^2 n
is less than epsilon. Since this
numerator is a constant as far as n is
concerned, the limit as n goes to
infinity of this would be zero. So for
sufficiently large n, it is less than
epsilon. So just let n be large enough
to make that happen. We're going to
partition our interval into n pieces
where each uh element of the partition
is given by this expression right here.
Left end point a plus i * the total
length over n. This means that each
interval is of the same length b minus a
over n. If I have x i + 1 minus x i, the
a's cancel and you have i + one of this
term minus i of them making the

## 00:36

difference just b minus a overn. This is
what's known as a uniform partition
where every piece is the same length.
All right. So we've made our uniform
partition into n pieces. Each pieces of
width b minus a overn. Now on each
interval defined by this partition
because f ofx= x is just an increasing
function. The int is the value at the
left end point which is the left end
point and the soup is the value at the
right end point which is equal to the
right end point because f ofx equals x.
So we can now compute the upper minus
lower sums. Here's the upper sum. We sum
over all pieces of the partition. The
value at the right end point which is
simply the right end point times the
width of that piece of the partition
minus the lower sum. the value at the
left end point times the width of that
piece. Now, a lot of simplification
happens when I combine these sums.
They're over the same range of index i.
So, I can just smush them into a single

## 00:37

sum. They share this factor b minus a n.
Factor that out. You'll end up with a +
i * b - a n minus a + i -1 * b - a n.
The a minus a cancels out and I have I *
this width minus i -1 * this width which
gives me just b minus a n. And I had
already factored out a b minus a n
giving us the following. The upper sum
minus the lower sum is exactly b minus a
n * b minus a n or b minus a n squed.
But this is now being summed as i goes
from 1 to n. And observe there's no i in
what we're summing up. As far as the
index i is concerned, this is a
constant. What do you get when you sum
up a constant n times? n * that constant
cancels one factor of n from this
denominator. And we specifically chose n
to be large enough so that b minus a^ 2

## 00:38

n is less than epsilon. Therefore, the
upper minus lower sums for this uniform
partition on a great number of pieces is
less than epsilon.
Therefore, by our previous proposition,
the function f ofx= x is integraable.
So, a remark, a way of thinking about
the integral is that it adds up or
integrates lots of local information.
Okay, so f ofx at a particular point is
a local value. It tells you what is
happening there. And integration
integrates all of that information
together. It smooshes all that you know
about values of the function at local
points into some sort of global result
about what is happening from a to b. Now
the integral sign was chosen by linenets
to be the long s. It came from a notion
of summation. So that integral sign is
supposed to be a stretched out s. Now
unlike derivatives which are a local
piece of information, the derivative of
a function at a point is very much

## 00:39

dependent on what is happening to the
function nearby that point and only
nearby that point. Integrals have to do
with what a more global perspective.
What is happening at one particular
point is not really the issue. You want
to somehow
collect together or integrate
information about what the function is
doing all the way from A to B. So this
comes up when you are trying to answer
questions about total distance traveled
or average temperature or total charge
of something over a region. Collecting a
bunch of information about what is
happening pointwise into a statement
about what is happening in a region.
That's the classic integral problem.
Now when f is defined on a set s and the
interval from a to b is a subset we say
that the function f is darbo integraable
on the interval if the restriction to
that interval is integraable a
technicality that is barely worth
stating I mean we were always talking

## 00:40

about f being defined on an interval
what if it's defined on a larger set
simply restrict your function to the
interval in question and you're fine now
conflating darbo and remon integrability
again there are three exercises that
help join this together. We say that f
is in the set script r of the interval
and write the integral from a to b of f
to be the value of this integral. That
script r is coming from reman
integraable functions. We have talked
about darau integraable functions but
again because some exercises show
there's an equivalence we're just going
to talk about remon integ.
Now it's also useful to talk about the
integral from a to b even when a is
bigger than or equal to b. So you don't
actually have an interval from a to b.
So we simply define
if a is bigger than b define the
integral from b to a to be -1 times the

## 00:41

integral from a to b.
Also if a equals b in other words you
you have a degenerate interval of a
single point it doesn't matter what the
function f is the integral from a to a
of f is always taken to be zero.
Now if the variable of integration is
important some example might require you
to like really specify what variable of
integration you're working with. It
doesn't change the value of the
integral. If you call the variable x or
s or t, whatever
this d is telling you what the variable
is named. And here you have the
expression. So here you're saying x goes
from a to b and you integrate f ofx.
Here s goes from a to b and you
integrate f of s and so forth and so
forth and so forth. Clearly renaming the
variable doesn't really matter. When we
are not particularly concerned with the
name of the variable, we just leave it
out. And that's the notation here. the
integral from a to b of f.

## 00:42

So we began with a sort of what I call a
definition dump. What's a partition?
What's an upper sum? What's a lower sum?
What's the definition of dbo
integrability? Definition after
definition after definition. But the
most useful notion for establishing a
bunch of our results was that of a
refinement. If you have a partition and
you add a finite number of points to it,
you have made a refinement of the
partition. And critically, refining a
partition only brings the upper and
lower sums closer in value. The lower
sum can come up, the upper sum can come
down. They don't cross each other. They
don't have to change. Note, but going to
a refinement only brings these values
closer together.
Uh we didn't formally define remon
times. The equivalence with Darbo
integraability is established in some of
the exercises and we're not putting the
exercises into the main body of these
