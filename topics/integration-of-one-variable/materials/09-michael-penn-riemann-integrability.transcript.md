## 00:00

now we're finally ready to look at the
definition of integrability
so let's get to it so let's say we've
got a bounded function
f from an interval a b to r
and then we set this thing script p
equal to the set of all partitions of
a b then we're going to define two
the upper integral and the lower
integral so the upper integral of
f on this interval is the infimum
of all upper sums as we let this
range over all partitions of a b and
then the lower integral
is going to be the supremum of all of
lower sums as again we let this
partition range over all partitions of
a b finally we say that f
is riemann integrable if
the lower integral is equal to the upper
integral and in that case
we give it a new notation which is
probably familiar from calculus so this

## 00:01

is the integral from a to b
of f we're going to start by proving a
pretty simple observation but i think
this is important to see the kind of
tools that we'll use
so we're going to prove that the lower
integral of f is always
less than or equal to the upper integral
of f
we're going to do this by way of
so in other words we're going to suppose
that the upper integral of
f is strictly less than the lower
integral of f
and then see that something goes wrong
there okay
good so notice that the upper integral
of f
that is going to be the infimum of all
of these
upper sums so i want to use the fact
that since u of f is strictly less than
l of f there exists
a partition p maybe we'll call it p1
of a b
such that the following is true we have

## 00:02

u of
f is less than or equal to u f
comma p which is strictly less than l
of f so in other words we can find a
where that upper sum of the partition
fits in between this u
f and this l f and so why can we do that
so if this were not possible then we
would contradict
the definition of the in femum which is
built into this upper
integral okay now we're going to do the
same kind of thing
but we're going to do it with l of f
so let's say here that there also exists
some partition p2 of a
b such that u of f
is less than or equal to uf p1
which is strictly less than l f
p 2 which is less than or equal to l
of f and again that's by the definition

## 00:03

of this lower integral via the supremum
so if we could not find such a partition
then this lower thing would not have
been the supremum
okay great so now let's see what we've
got we've got
two partitions p1 and p2
where the upper sum over one partition
smaller than the lower sum over the
other partition
but we know for a fact this was proven
in the last video
that the lower sum of f over a partition
is always less than or equal to the
upper sum of
f over any other partition
but that provides us with our
because this inequality and this
inequality are not compatible
okay great so let's maybe get rid of
this and then we're going to prove a
nice theorem that classifies
when a function is integrable so just
like with many definitions in
often proving something via the

## 00:04

definition is a bit tricky
and what you need is some sort of more
calculational approach
and often there are theorems that go and
prove that this calculational approach
is equivalent to the definition that's
what we've got here
so f which is still a bounded function
is riemann integrable i left off the
word riemann but
anytime we say integrable for the time
being it will be riemann integrable
on the interval a b if and only if
for all epsilon bigger than 0 there is a
p epsilon of a b such that
the upper sum of f on that partition
minus the lower sum of the f on that
partition is less than epsilon
now maybe i want to point out real quick
that the upper
sum is always bigger than or equal to
the lower sum
so we know that this is going to be
always bigger than or equal to 0
in the first place so this is bound
between zero and epsilon
but since epsilon can be made as small

## 00:05

as we want that means these two
quantities can be made as close together
as we want
so notice the right hand side of this if
and only if statement is very
whereas the left-hand side is built out
of this definition that we have over
okay so let's maybe get to the proof so
since this is an if and only if
statement we need to do two directions
so let's start with the reverse
so we're gonna begin by taking
any epsilon bigger than zero and then
finding our partition p epsilon
such that this inequality is satisfied
so we've got 0 is less than or equal to
u f
p epsilon minus l f
p epsilon which is less than epsilon
great so again we're working backwards
or the reverse direction so we can
assume that this kind of thing is
now we're going to use the following
string of inequalities which is always

## 00:06

and that goes like this l f p
epsilon is always going to be less than
or equal to
l of f so in other words the lower sum
is always less than or equal to the
lower integral
that's because this lower integral is
the supremum of
all such lower sums but now that's less
than or equal to
u of f by our previous observation
but now that's less than or equal to u f
p epsilon again because
the upper integral is always less than
or equal to the upper sum
given that the upper integral is the
infimum over all such
possible upper sums but now we can look
at this
string of inequalities and
use the fact that these two are close
together to force
these two close together in other words
we have the following set up
we have u of f minus

## 00:07

l of f is less than or equal to u
f p epsilon minus l
f p epsilon but that's less than epsilon
and then i guess i should maybe say over
here that all of this is bigger than or
equal to zero
so let's see what we've got going on
here we've got this
arbitrary epsilon bigger than zero
and after taking this arbitrary epsilon
bigger than zero
we have shown that the difference of the
upper integral and the lower integral
is bound between zero and epsilon so in
other words
we can make this difference between the
upper integral and lower integral as
small as we want
they are arbitrarily close together
but from one of the maybe first theorems
that we proved in the whole class
that tells us that these two numbers uf
and lf
are the same and that finishes this
reverse direction
okay let's maybe do the forward

## 00:08

direction now
now we're ready for this reverse
direction so we want to suppose
that f is bounded and
riemann integrable so i'll just say
on our interval a b
good and then next we also want to be
some arbitrary epsilon bigger than zero
and then our goal is to find this
partition that makes this inequality
okay so we want to do two things first
and that is find a partition related to
the upper integral and the lower
so let's first find p1
a partition of a b such that
the following inequality is true we have
p1 in other words that upper sum of f
on p1 is less than
u f plus epsilon over two

## 00:09

so let's maybe talk our way through why
we can do that
well if that were not possible that
would contradict
the definition of uf by the end femum
and actually this kind of construction
was something really
familiar that we did at the very very
beginning of the class
okay great and then next we want to find
a partition p2 such that we've got a
but different inequality for the lower
sum and lower integral
and in this case we want lf p2
to be bigger than lf minus epsilon over
and again that's by the definition of
the supremum
or the um least upper bound okay great
now what we want to do is form a
out of p1 and p2 and this is going to be
the so-called common refinement
and we'll call that common refinement
piece of epsilon so that'll be our

## 00:10

partition that we want so we've got p
sub epsilon equals p1
union p2 so like i said this is the
refinement of p1 and p2 look in one of
the previous videos if you need a
reminder of what the
refinement of a partition is now let's
at our goal thing right here so we have
is less than or equal to u f
p epsilon minus l f p epsilon
so we know that this is going to be
bigger than or equal to zero just by the
definition of the upper sum and the
lower sum
but next thing that i want to do is
replace u f p epsilon
with this thing that is larger and i'll
l f p epsilon with this thing that is
but that's going to keep my inequality
going in the correct direction
because i have minus lfp epsilon
so in fact i'm going to use this fact
right here that minus
lf p epsilon is in fact

## 00:11

less than epsilon over two
minus l of f just
multiplying by the minus one changes the
direction but now we can just like
essentially add these two inequalities
and we're done
so let's see what we get when we do that
so here we will get that this is
strictly less
than u of f minus l of
f plus epsilon over two plus epsilon
over two
but we know that u of f and l of f are
the same because we have assumed
integrability of our function
f so that turns out to be epsilon over
plus epsilon over 2 which is epsilon
so in the end we have our desired
inequality to finish off this forward
okay let's get rid of this and we're
going to do one more theorem we're going
to finish this video off by looking at a
classic and very important theorem
so this says that if f is continuous on
a closed interval a b

## 00:12

then it is integrable on this closed
interval as well
so i first want to notice that
continuity plus
the compactness of this closed interval
implies that f is uniformly continuous
on a b
so let's maybe notice that first so f
is uniformly continuous
on our interval a b
again because continuity plus
compactness of the domain
implies uniform continuity okay
so next we want to be given epsilon
bigger than zero and our
goal is to form a partition that makes
the upper sum minus the lower sum
over that partition less than epsilon
but we need to use this continuity in
fact we want to use this
uniform continuity so let's go ahead
and take delta bigger than 0
such that if the absolute value of x

## 00:13

minus y is less than delta where x and y
are both on the interval a b but they're
within delta of each other
we have the absolute value of f of x
minus f of y is less than not just
epsilon but epsilon over b minus a so
again this delta is brought into
existence because of the uniform
continuity of f on a b that's why it
works for all
x and y within delta of each other
okay great now we're going to start
constructing our partition
there's a bunch of ways to do this i'm
going to do this a very concrete way
so let's go ahead and find some
natural number which i'll call n
such that b minus
a over n is less than delta
and so that's possible by the
archimedean principle because you can
uh move this around until you get n is

## 00:14

bigger than some real number but you
know you can always find a natural
number bigger than any real number
but again this is the kind of stuff that
we do all the time at this point
okay so next we want to define the
points in our partition
so i'm going to define them like this
we'll set x
i equal to a plus
i times b
minus a over n good
so this is like a plus i delta x like
you might have seen in a calculus 2 type
now what i want to notice here is that x
i minus x i minus 1 is going to be less
than delta
and that's going to be true for all i in
fact this
actually partitions it into equal spaced
points which is not necessary at all but
that's what happens here
okay now next we're going to consider
the following partition
p which is going to be equal to x 0
which is
a so i'm just setting x 0 equal to a

## 00:15

and then i've got x 1 x 2 all the way up
to x
n but x n is equal to b by this
definition right here
now next i'm going to look at the upper
sum of f
on this partition and the lower sum of f
on this partition and i'm going to take
their difference
so let's go ahead and do that we've got
u f p
minus l f p like that so
again let's go ahead and really get into
the definition here
so this is going to be the sum as i goes
1 to n of capital m sub
i minus little m sub i
times x sub i minus x sub i minus 1.
so i mash together the definition of the
upper sum and the lower sum but
that's not really much okay nice
but next we can use the fact that
by the extreme value theorem the

## 00:16

continuity of f
and uh the closed interval tells us
that f achieves both its maximum
and its minimum or its supremum and its
in femum
those are the same when you're working
over a compact set and a continuous
on each sub interval so
in other words we can find some point
we could call it maybe y i that
achieves this number and some point
maybe we could call it z
i that achieves that number so that
tells us that this
is going to be equal to the sum as i
goes from
1 to n of f of
y i minus f of z
i and then this is going to be times x
i minus x i minus 1.
so let's maybe go ahead and point out
over here
exactly what we've done so here we have

## 00:17

y i is on the interval x i minus 1
x i where f
of y i is this capital m
i in other words it's the supremum of
f over that sub interval again we know
that as possible because
we have the extreme value theorem and
z i well that's going to be on this same
interval but now that's the point where
achieves its infimum or its minimum so
lowercase mi like that
then the next thing that i want to
notice is that by this
setup we have the absolute value of
y i minus z i is less than
delta and we know that
just because these y i's and zi's are
these two numbers those of which are
within delta of each other

## 00:18

but what that tells us is that this
is less than epsilon over b minus a
so that means we can bring that out of
this whole thing if we introduce an
inequality so just to reiterate
all of these are going to be less than
epsilon over
b minus a from our construction right
here because these
points y i and z i are close enough to
each other so we've got
this is less than epsilon over b minus a
and now we've got the sum
as i goes from 1 to n of x i
minus x i minus 1. cool
but now that's a telescoping sum and so
telescopes just to xn minus x0
so that's pretty easy to see but xn
minus x0 is exactly b
minus a so that's going to cancel out
this denominator
and we get that this sum is now equal to
that actually finishes off the proof

## 00:19

because we constructed a partition
p where the upper sum of f on that
partition minus the lower sum of
f on that partition is less than epsilon
and that was for this arbitrary epsilon
that we took at the top
okay that's a good place to stop
