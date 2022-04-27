from pydoc_data.topics import topics


topics=[
    '''Although BCNF removes any anomalies due to functional dependencies, further
research led to the identification of another type of dependency called a Multi-
Valued Dependency (MVD), which can also cause data redundancy (Fagin, 1977).
In this section, we briefly describe a multi-valued dependency and the association
of this type of dependency with Fourth Normal Form (4NF).
|
493494
|
Chapter 15  Advanced Normalization
Figure 15.8(a) The BranchStaffOwner relation.
15.4.1 Multi-Valued Dependency
The possible existence of multi-valued dependencies in a relation is due to 1NF,
which disallows an attribute in a tuple from having a set of values. For example, if
we have two multi-valued attributes in a relation, we have to repeat each value of
one of the attributes with every value of the other attribute, to ensure that tuples of
the relation are consistent. This type of constraint is referred to as a multi-valued
dependency and results in data redundancy. Consider the BranchStaffOwner relation
shown in Figure 15.8, which displays the names of members of staff (sName) and
property owners (oName) at each branch office (branchNo). In this example, assume
that staff name (sName) uniquely identifies each member of staff and that the owner
name (oName) uniquely identifies each owner.
In this example, members of staff called Ann Beech and David Ford work at
branch B003, and property owners called Carol Parrel and Tina Murphy are regis-
tered at branch B003. However, as there is no direct relationship between members
of staff and property owners at a given branch office, we must create a tuple for every
combination of member of staff and owner to ensure that the relation is consistent.
Multi-Valued
Dependency
(MVD)
Represents a dependency between attributes (for example, A, B,
and C) in a relation, such that for each value of A there is a set of
values for B and a set of values for C. However, the set of values
for B and C are independent of each other.
We represent a MVD between attributes A, B, and C in a relation using the fol-
lowing notation:
A—
>> B
A—
>> C
A multi-valued dependency constraint potentially exists in the BranchStaffOwner
relation, because two independent 1:* relationships are represented in the same
relation. We specify the MVD constraint in the BranchStaffOwner relation shown in
Figure 15.8(a) as follows:
branchNo —
>> sName
branchNo —
>> oName
A multi-valued dependency can be further defined as being trivial or nontrivial. A
MVD A —
>> B in relation R is defined as being trivial if (a) B is a subset of A or (b)
A < B = R. A MVD is defined as being nontrivial if neither (a) nor (b) are satisfied.
A trivial MVD does not specify a constraint on a relation; a nontrivial MVD does
specify a constraint.15.5
Fifth Normal Form (5NF)
Figure 15.8(b) The BranchStaff and BranchOwner 4NF relations.
The BranchStaffOwner relation shown in Figure 15.8(a) contains two nontrivial
dependencies that is branchNo —
>> sName and branchNo —
>> oName with branchNo not
a candidate key of the relation. The BranchStaffOwner relation is therefore constrained
by the nontrivial MVDs to repeat rows to ensure that the relation remains consistent in
terms of the relationship between the sName and oName attributes. For example, if we
wanted to add a new property owner for branch B003, we would have to create two new
tuples, one for each member of staff, to ensure that the relation remains consistent. This
is an example of an update anomaly caused by the presence of the nontrivial MVDs. We
therefore clearly require a normal form that prevents relational structures such as the
BranchStaffOwner relation.
15.4.2 Definition of Fourth Normal Form
Fourth Normal
Form (4NF)
A relation is in 4NF if and only if for every nontrivial multi-
valued dependency A —
>> B, A is a candidate key of the relation.
Fourth normal form (4NF) prevents a relation from containing a nontrivial MVD
without the associated determinant being a candidate key for the relation (Fagin,
1977). When the 4NF rule is violated, the potential for data redundancy exists,
as shown previously in Figure 15.8(a). The normalization of a relation breaking
the 4NF rule requires the removal of the offending MVD from the relation by
placing the multi-valued attribute(s) in a new relation along with a copy of the
determinant.
For example, the BranchStaffOwner relation in Figure 15.8(a) is not in 4NF,
because of the presence of two nontrivial MVDs. We decompose the BranchStaffOwner
relation into the BranchStaff and BranchOwner relations, as shown in Figure 15.8(b).
Both new relations are in 4NF, because the BranchStaff relation contains the trivial
MVD branchNo —
>> sName, and the BranchOwner relation contains the trivial MVD
branchNo —
>> oName. Note that the 4NF relations do not display data redundancy,
and the potential for update anomalies is removed. For example, to add a new
property owner for branch B003, we simply create a single tuple in the BranchOwner
relation. For a detailed discussion on 4NF, the interested reader is referred to Date
(2012) and Elmasri and Navathe (2010).''',
'''Whenever we decompose a relation into two relations, the resulting relations have
the lossless-join property. This property refers to the ability to rejoin the resulting
|
495496
|
Chapter 15  Advanced Normalization
relations to produce the original relation. However, there are cases in which there
is a requirement to decompose a relation into more than two relations. Although
rare, these cases are managed by join dependency and Fifth Normal Form (5NF).
In this section we briefly describe the lossless-join dependency and the association
with 5NF.
15.5.1 Lossless-Join Dependency
Lossless-join
dependency
A property of decomposition that ensures that no spurious tuples
are generated when relations are reunited through a natural join
operation.
In splitting relations by projection, we are very explicit about the method of decom-
position. In particular, we are careful to use projections that can be reversed by
joining the resulting relations, so that the original relation is reconstructed. Such
a decomposition is called a lossless-join (also called a nonloss- or nonadditive-join)
decomposition, because it preserves all the data in the original relation and does
not result in the creation of additional spurious tuples. For example, Figures
15.8(a) and 15.8(b) show that the decomposition of the BranchStaffOwner relation
into the BranchStaff and BranchOwner relations has the lossless-join property. In other
words, the original BranchStaffOwner relation can be reconstructed by performing a
natural join operation on the BranchStaff and BranchOwner relations. In this exam-
ple, the original relation is decomposed into two relations. However, there are
cases were we require to perform a lossless-join decompose of a relation into more
than two relations (Aho et al., 1979). These cases are the focus of the lossless-join
dependency and 5NF.
15.5.2 Definition of Fifth Normal Form
Fifth Normal
Form (5NF)
A relation is in 5NF if and only if for every join dependency (R1,
R2, . . . Rn) in a relation R, each projection includes a candidate
key of the original relation.
Fifth normal form (5NF) prevents a relation from containing a nontrivial join
dependency (JD) without the associated projection including a candidate key of the
original relation (Fagin, 1977). Nontrivial JDs that are not associated with candi-
date keys are very rare, so 4NF relations are normally also in 5NF.
Although rare, let us examine what potential problems exist for a relation that
breaks the rules of 5NF. The PropertyItemSupplier relation shown in Figure 15.9(a)
is not in 5NF, as it contains a nontrivial join dependency constraint. This relation
describes properties (propertyNo) that require certain items (itemDescription), which
are supplied by suppliers (supplierNo) to the properties (propertyNo). Furthermore,
whenever a property (p) requires a certain item (i), and a supplier (s) supplies that
item (i), and the supplier (s) already supplies at least one item to that property (p),
then the supplier (s) will also supply the required item (i) to property (p). In this
example, assume that a description of an item (itemDescription) uniquely identifies
each type of item.15.5
Fifth Normal Form (5NF)
|
497
Figure 15.9
(a) Illegal state
for Propertyltem-
Supplier relation
and (b) legal state
for Propertyltem-
Supplier relation.
To identify the type of constraint on the PropertyltemSupplier relation in Figure
15.9(a), consider the following statement:
Property PG4 requires Bed
(from data in tuple 1)
Supplier S2 supplies property PG4
(from data in tuple 2)
Supplier S2 provides Bed
(from data in tuple 3)
Then Supplier S2 provides Bed for property PG4
If
This example illustrates the cyclical nature of the constraint on the PropertyltemSupplier
relation. If this constraint holds then the tuple (PG4, Bed, S2) must exist in any
legal state of the PropertyltemSupplier relation, as shown in Figure 15.9(b). This is an
example of a type of update anomaly and we say that this relation contains a non-
trivial join dependency (JD) constraint.
Join
dependency
(JD)
Describes a type of dependency. For example, for a relation R
with subsets of the attributes of R denoted as A, B, . . . , Z, a relation
R satisfies a join dependency if and only if every legal value of R is
equal to the join of its projections on A, B, . . . , Z.
As the PropertyltemSupplier relation contains a join dependency, it is therefore not
in 5NF. To remove the join dependency, we decompose the PropertyltemSupplier
relation into three 5NF relations—namely, Propertyltem (R1), ItemSupplier (R2),
and PropertySupplier (R3) relations—as shown in Figure 15.10. We say that the
PropertyltemSupplier relation with the form (A, B, C) satisfies the join dependency JD
(R1(A, B), R2(B, C), R3(A, C)).
It is important to note that performing a natural join on any two relations will pro-
duce spurious tuples; however, performing the join on all three will recreate the original
PropertyltemSupplier relation.
For a detailed discussion on 5NF, the interested reader is referred to Date (2012) and
Elmasri and Navathe (2010).''',
'''A trigger defines an action that the database should take when some event occurs
in the application. A trigger may be used to enforce some referential integrity con-
straints, to enforce complex constraints, or to audit changes to data. The general
format of a trigger in SQL is:
CREATE TRIGGER TriggerName
BEFORE | AFTER | INSTEAD OF
INSERT | DELETE | UPDATE [OF TriggerColumnList]
|
281282
|
Chapter 8  Advanced SQL
ON TableName
[REFERENCING {OLD | NEW} AS {OldName | NewName}
[FOR EACH {ROW | STATEMENT}]
[WHEN Condition]
<trigger action>
This is not the complete definition, but it is sufficient to demonstrate the basic con-
cept. The code within a trigger, called the trigger body or trigger action, is made up
of an SQL block. Triggers are based on the Event–Condition–Action (ECA) model:
• The event (or events) that trigger the rule, which can be an INSERT, UPDATE, or
DELETE statement on a specified table (or possibly view). In Oracle, it can also be:
– a CREATE, ALTER, or DROP statement on any schema object;
– a database startup or instance shutdown, or a user logon or logoff;
– a specific error message or any error message.
It is also possible to specify whether the trigger should fire before the event or
after the event.
• The condition that determines whether the action should be executed. The condition
is optional but, if specified, the action will be executed only if the condition is true.
• The action to be taken. This block contains the SQL statements and code to be
executed when a triggering statement is issued and the trigger condition evalu-
ates to true.
There are two types of trigger: row-level triggers (FOR EACH ROW) that execute
for each row of the table that is affected by the triggering event, and statement-level
triggers (FOR EACH STATEMENT) that execute only once even if multiple rows
are affected by the triggering event. SQL also supports INSTEAD OF triggers,
which provide a transparent way of modifying views that cannot be modified directly
through SQL DML statements (INSERT, UPDATE, and DELETE). These triggers
are called INSTEAD OF triggers because, unlike other types of trigger, the trigger
is fired instead of executing the original SQL statement. Triggers can also activate
themselves one after the other. This can happen when the trigger action makes a
change to the database that has the effect of causing another event that has a trigger
associated with it to fire.
Example 8.2
AFTER Row-level trigger
Create an AFTER row-level trigger to keep an audit trail of all rows inserted into the Staff table.
CREATE TRIGGER StaffAfterInsert
AFTER INSERT ON Staff
REFERENCING NEW AS new
FOR EACH ROW
BEGIN
INSERT INTO StaffAudit
VALUES (:new.staffNo, :new.fName, :new.lName, :new.position,
:new.sex, :new.DOB, :new.salary, :new.branchNo);
END;
Note that the SQL standard uses NEW ROW instead of NEW and OLD ROW instead of
OLD.8.3
Example 8.3
Triggers
Using a BEFORE trigger
DreamHome has a rule that prevents a member of staff from managing more than 100
properties at the same time. We could create the trigger shown in Figure 8.4 to enforce
this constraint. This trigger is invoked before a row is inserted into the PropertyForRent
Figure 8.4 Trigger to enforce the constraint that a member of staff cannot manage more than
100 properties at any one time.
table or an existing row is updated. If the member of staff currently manages 100 prop-
erties, the system displays a message and aborts the transaction. The following points
should be noted:
• The BEFORE keyword indicates that the trigger should be executed before an insert
is applied to the PropertyForRent table.
• The FOR EACH ROW keyword indicates that this is a row-level trigger, which
executes for each row of the PropertyForRent table that is updated in the statement.
Example 8.4
Using triggers to enforce referential integrity
By default, Oracle enforces the referential actions ON DELETE NO ACTION and ON
UPDATE NO ACTION on the named foreign keys (see Section 7.2.4). It also allows
the additional clause ON DELETE CASCADE to be specified to allow deletions from
the parent table to cascade to the child table. However, it does not support the ON
UPDATE CASCADE action, or the SET DEFAULT and SET NULL actions. If any of
these actions are required, they will have to be implemented as triggers or stored pro-
cedures, or within the application code. For example, from Example 7.1 the foreign key
staffNo in the PropertyForRent table should have the action ON UPDATE CASCADE. This
action can be implemented using the triggers shown in Figure 8.5.
Trigger 1 (PropertyForRent_Check_Before)
The trigger in Figure 8.5(a) is fired whenever the staffNo column in the PropertyForRent
table is updated. The trigger checks before the update takes place whether the new value
specified exists in the Staff table. If an Invalid_Staff exception is raised, the trigger issues
an error message and prevents the change from occurring.
|
283284
|
Chapter 8  Advanced SQL
Figure 8.5(a) Oracle triggers to enforce ON UPDATE CASCADE on the foreign key staffNo in
the PropertyForRent table when the primary key staffNo is updated in the Staff table:
(a) trigger for the PropertyForRent table.8.3
Triggers
Changes to support triggers on the Staff table
The three triggers shown in Figure 8.5(b) are fired whenever the staffNo column in
the Staff table is updated. Before the definition of the triggers, a sequence number
­updateSequence is created, along with a public variable updateSeq (which is accessible
to the three triggers through the seqPackage package). In addition, the PropertyForRent
table is modified to add a column called updateId, which is used to flag whether a row
has been updated, to prevent it from being updated more than once during the cascade
operation.
Figure 8.5(b) Triggers for the Staff table.
|
285286
|
Chapter 8  Advanced SQL
Trigger 2 (Cascade_StaffNo_Update1)
This (statement-level) trigger fires before the update to the staffNo column in the Staff
table to set a new sequence number for the update.
Trigger 3 (Cascade_StaffNo_Update2)
This (row-level) trigger fires to update all rows in the PropertyForRent table that have the
old staffNo value (:old.staffNo) to the new value (:new.staffNo), and to flag the row as
having been updated.
Trigger 4 (Cascade_StaffNo_Update3)
The final (statement-level) trigger fires after the update to reset the flagged rows back
to unflagged.
Dropping triggers
Triggers can be dropped using the DROP TRIGGER <TriggerName> statement.
TRIGGER Privilege
In order to create a trigger on a table, the user either has to be the owner of the table
(in which case the user will inherit the TRIGGER privilege) or the user will need to have
been granted the TRIGGER privilege on the table (see Section 7.6).
Advantages and disadvantages of triggers
There are a number of advantages and disadvantages with database triggers. Advantages
of triggers include:
• Elimination of redundant code. Instead of placing a copy of the functionality of the trig-
ger in every client application that requires it, the trigger is stored only once in the
database.
• Simplifying modifications. Changing a trigger requires changing it in one place only;
all the applications automatically use the updated trigger. Thus, they are only coded
once, tested once, and then centrally enforced for all the applications accessing the
database. The triggers are usually controlled, or at least audited, by a skilled DBA.
The result is that the triggers can be implemented efficiently.
• Increased security. Storing the triggers in the database gives them all the benefits of
security provided automatically by the DBMS.
• Improved integrity. Triggers can be extremely useful for implementing some types of
integrity constraints, as we have demonstrated earlier. Storing such triggers in the
database means that integrity constraints can be enforced consistently by the DBMS
across all applications.
• Improved processing power. Triggers add processing power to the DBMS and to the
database as a whole.
• Good fit with the client-server architecture. The central activation and processing of trig-
gers fits the client-server architecture well (see Chapter 3). A single request from
a client can result in the automatic performing of a whole sequence of checks and
subsequent operations by the database server. In this way, performance is potentially
improved as data and operations are not transferred across the network between the
client and the server.
Triggers also have disadvantages, which include:
• Performance overhead. The management and execution of triggers have a performance
overhead that have to be balanced against the advantages cited previously.8.4
Recursion
• Cascading effects. The action of one trigger can cause another trigger to be fired, and
so on, in a cascading manner. Not only can this cause a significant change to the
database, but it can also be hard to foresee this effect when designing the trigger.
• Cannot be scheduled. Triggers cannot be scheduled; they occur when the event that they
are based on happens.
• Less portable. Although now covered by the SQL standard, most DBMSs implement
their own dialect for triggers, which affects portability''',
'''An early proposal for a standard terminology and general architecture for database
systems was produced in 1971 by the DBTG appointed by CODASYL in 1971.
The DBTG recognized the need for a two-level approach with a system view called
the schema and user views called subschemas. The American National Standards
Institute (ANSI) Standards Planning and Requirements Committee (SPARC),
or ANSI/X3/SPARC, produced a similar terminology and architecture in 1975
(ANSI, 1975). The ANSI-SPARC architecture recognized the need for a three-level
approach with a system catalog. These proposals reflected those published by the
IBM user organizations Guide and Share some years previously, and concentrated
on the need for an implementation-independent layer to isolate programs from
underlying representational issues (Guide/Share, 1970). Although the ANSI-SPARC
model did not become a standard, it still provides a basis for understanding some
of the functionality of a DBMS.
For our purposes, the fundamental point of these and later reports is the iden-
tification of three levels of abstraction, that is, three distinct levels at which data
items can be described. The levels form a three-level architecture comprising an
external, a conceptual, and an internal level, as depicted in Figure 2.1. The way
users perceive the data is called the external level. The way the DBMS and the
operating system perceive the data is the internal level, where the data is actually
stored using the data structures and file organizations described in Appendix F.
The conceptual level provides both the mapping and the desired independence
between the external and internal levels.
The objective of the three-level architecture is to separate each user’s view of the
database from the way the database is physically represented. There are several
reasons why this separation is desirable:
• Each user should be able to access the same data, but have a different customized
view of the data. Each user should be able to change the way he or she views the
data, and this change should not affect other users.2.1
The Three-Level ANSI-SPARC Architecture
|
85
Figure 2.1
The ANSI-
SPARC three-
level architecture.
• Users should not have to deal directly with physical database storage details, such
as indexing or hashing (see Appendix F). In other words, a user’s interaction with
the database should be independent of storage considerations.
• The DBA should be able to change the database storage structures without affect-
ing the users’ views.
• The internal structure of the database should be unaffected by changes to the
physical aspects of storage, such as the changeover to a new storage device.
• The DBA should be able to change the conceptual structure of the database with-
out affecting all users.
2.1.1 External Level
External
level
The users’ view of the database. This level describes that part of the
database that is relevant to each user.
The external level consists of a number of different external views of the database.
Each user has a view of the “real world” represented in a form that is familiar for
that user. The external view includes only those entities, attributes, and relation-
ships in the “real world” that the user is interested in. Other entities, attributes, or
relationships that are not of interest may be represented in the database, but the
user will be unaware of them.
In addition, different views may have different representations of the same
data. For example, one user may view dates in the form (day, month, year), while
another may view dates as (year, month, day). Some views might include derived
or calculated data: data not actually stored in the database as such, but created
when needed. For example, in the DreamHome case study, we may wish to view the
age of a member of staff. However, it is unlikely that ages would be stored, as this
data would have to be updated daily. Instead, the member of staff’s date of birth
would be stored and age would be calculated by the DBMS when it is referenced.86
|
Chapter 2  Database Environment
Views may even include data combined or derived from several entities. We discuss
views in more detail in Sections 4.4 and 7.4.
2.1.2 Conceptual Level
Conceptual
level
The community view of the database. This level describes what data
is stored in the database and the relationships among the data.
The middle level in the three-level architecture is the conceptual level. This level
contains the logical structure of the entire database as seen by the DBA. It is a com-
plete view of the data requirements of the organization that is independent of any
storage considerations. The conceptual level represents:
• all entities, their attributes, and their relationships;
• the constraints on the data;
• semantic information about the data;
• security and integrity information.
The conceptual level supports each external view, in that any data available to a
user must be contained in, or derivable from, the conceptual level. However, this
level must not contain any storage-dependent details. For instance, the descrip-
tion of an entity should contain only data types of attributes (for example,
inte­ger, real, character) and their length (such as the maximum number of digits
or characters), but not any storage considerations, such as the number of bytes
occupied.
2.1.3 Internal Level
Internal
level
The physical representation of the database on the computer. This
level describes how the data is stored in the database.
The internal level covers the physical implementation of the database to achieve
optimal runtime performance and storage space utilization. It covers the data
structures and file organizations used to store data on storage devices. It inter-
faces with the operating system access methods (file management techniques for
storing and retrieving data records) to place the data on the storage devices, build
the indexes, retrieve the data, and so on. The internal level is concerned with such
things as:
• storage space allocation for data and indexes;
• record descriptions for storage (with stored sizes for data items);
• record placement;
• data compression and data encryption techniques.
Below the internal level there is a physical level that may be managed by the
operating system under the direction of the DBMS. However, the functions of
the DBMS and the operating system at the physical level are not clear-cut and
vary from system to system. Some DBMSs take advantage of many of the operating2.1
The Three-Level ANSI-SPARC Architecture
system access methods, and others use only the most basic ones and create their
own file organizations. The physical level below the DBMS consists of items that
only the operating system knows, such as exactly how the sequencing is imple-
mented and whether the fields of internal records are stored as contiguous bytes
on the disk.
2.1.4 Schemas, Mappings, and Instances
The overall description of the database is called the database schema. There are
three different types of schema in the database and these are defined according
to the levels of abstraction of the three-level architecture illustrated in Figure 2.1.
At the highest level, we have multiple external schemas (also called subschemas)
that correspond to different views of the data. At the conceptual level, we have the
conceptual schema, which describes all the entities, attributes, and relationships
together with integrity constraints. At the lowest level of abstraction we have the
internal schema, which is a complete description of the internal model, containing
the definitions of stored records, the methods of representation, the data fields,
and the indexes and storage structures used. There is only one conceptual schema
and one internal schema per database.
The DBMS is responsible for mapping between these three types of schema.
It must also check the schemas for consistency; in other words, the DBMS must
confirm that each external schema is derivable from the conceptual schema,
and it must use the information in the conceptual schema to map between each
external schema and the internal schema. The conceptual schema is related to
the internal schema through a conceptual/internal mapping. This mapping
enables the DBMS to find the actual record or combination of records in physi-
cal storage that constitute a logical record in the conceptual schema, together
with any constraints to be enforced on the operations for that logical record.
It also allows any differences in entity names, attribute names, attribute order,
data types, and so on to be resolved. Finally, each external schema is related to
the conceptual schema by the external/conceptual mapping. This mapping
enables the DBMS to map names in the user’s view to the relevant part of the
conceptual schema.
An example of the different levels is shown in Figure 2.2. Two different external
views of staff details exist: one consisting of a staff number (sNo), first name (fName),
last name (IName), age, and salary; a second consisting of a staff number (staffNo),
last name (IName), and the number of the branch the member of staff works at
(branchNo). These external views are merged into one conceptual view. In this
merging process, the major difference is that the age field has been changed into
a date of birth field, DOB. The DBMS maintains the external/conceptual mapping;
for example, it maps the sNo field of the first external view to the staffNo field of
the conceptual record. The conceptual level is then mapped to the internal level,
which contains a physical description of the structure for the conceptual record. At
this level, we see a definition of the structure in a high-level language. The structure
contains a pointer, next, which allows the list of staff records to be physically linked
together to form a chain. Note that the order of fields at the internal level is differ-
ent from that at the conceptual level. Again, the DBMS maintains the conceptual/
internal mapping.
|
8788
|
Chapter 2  Database Environment
Figure 2.2
Differences between the three levels.
It is important to distinguish between the description of the database and the
database itself. The description of the database is the database schema. The
schema is specified during the database design process and is not expected to
change frequently. However, the actual data in the database may change frequently;
for example, it changes every time we insert details of a new member of staff or a
new property. The data in the database at any particular point in time is called a
database instance. Therefore, many database instances can correspond to the same
database schema. The schema is sometimes called the intension of the database; an
instance is called an extension (or state) of the database.
2.1.5 Data Independence
A major objective for the three-level architecture is to provide data independence,
which means that upper levels are unaffected by changes to lower levels. There are
two kinds of data independence: logical and physical.
Logical data
independence
The immunity of the external schemas to changes in the
conceptual schema.
Changes to the conceptual schema, such as the addition or removal of new entities,
attributes, or relationships, should be possible without having to change existing
external schemas or having to rewrite application programs. Clearly, the users for
whom the changes have been made need to be aware of them, but what is important
is that other users should not be.
Physical data
independence
The immunity of the conceptual schema to changes in the
internal schema.2.2
Database Languages
|
Figure 2.3
Data indepen­
dence and the
ANSI-SPARC
three-level
architecture.
Changes to the internal schema, such as using different file organizations or stor-
age structures, using different storage devices, modifying indexes or hashing algo-
rithms, should be possible without having to change the conceptual or external
schemas. From the users’ point of view, the only effect that may be noticed is a
change in performance. In fact, deterioration in performance is the most common
reason for internal schema changes. Figure 2.3 illustrates where each type of data
independence occurs in relation to the three-level architecture.
The two-stage mapping in the ANSI-SPARC architecture may be inefficient, but
it also provides greater data independence. However, for more efficient mapping,
the ANSI-SPARC model allows the direct mapping of external schemas onto
the internal schema, thus by-passing the conceptual schema. This mapping of
course reduces data independence, so that every time the internal schema
changes, the external schema and any dependent application programs may also
have to change.''',
'''We now examine the constraints that may be placed on entity types that par-
ticipate in a relationship. The constraints should reflect the restrictions on the
relationships as perceived in the “real world.” Examples of such constraints
include the requirements that a property for rent must have an owner and each
branch must have staff. The main type of constraint on relationships is called
multiplicity.
Multiplicity
The number (or range) of possible occurrences of an entity type
that may relate to a single occurrence of an associated entity type
through a particular relationship.
Multiplicity constrains the way that entities are related. It is a representation of
the policies (or business rules) established by the user or enterprise. Ensuring that
all appropriate constraints are identified and represented is an important part of
modeling an enterprise.
As we mentioned earlier, the most common degree for relationships is binary.
Binary relationships are generally referred to as being one-to-one (1:1), one-to-
many (1:*), or many-to-many (*:*). We examine these three types of relationships
using the following integrity constraints:
• a member of staff manages a branch (1:1);
• a member of staff oversees properties for rent (1:*);
• newspapers advertise properties for rent (*:*).
In Sections 12.6.1, 12.6.2, and 12.6.3 we demonstrate how to determine the
multiplicity for each of these constraints and show how to represent each in an ER
diagram. In Section 12.6.4 we examine multiplicity for relationships of degrees
higher than binary.
It is important to note that not all integrity constraints can be easily represented
in an ER model. For example, the requirement that a member of staff receives an
additional day's holiday for every year of employment with the enterprise may be
difficult to represent in an ER model.420
|
Chapter 12  Entity–Relationship Modeling
Figure 12.14(a)
Semantic net
showing two
occurrences of
the Staff Manages
Branch relationship
type.
12.6.1 One-to-One (1:1) Relationships
Consider the relationship Manages, which relates the Staff and Branch entity types.
Figure 12.14(a) displays two occurrences of the Manages relationship type (denoted
rl and r2) using a semantic net. Each relationship (rn) represents the association
between a single Staff entity occurrence and a single Branch entity occurrence. We
represent each entity occurrence using the values for the primary key attributes of
the Staff and Branch entities, namely staffNo and branchNo.
Determining the multiplicity
Determining the multiplicity normally requires examining the precise relationships
between the data given in a enterprise constraint using sample data. The sample
data may be obtained by examining filled-in forms or reports and, if possible, from
discussion with users. However, it is important to stress that to reach the right con-
clusions about a constraint requires that the sample data examined or discussed is
a true representation of all the data being modeled.
In Figure 12.14(a) we see that staffNo SG5 manages branchNo B003 and staffNo
SL21 manages branchNo BOO5, but staffNo SG37 does not manage any branch. In
other words, a member of staff can manage zero or one branch and each branch is
managed by one member of staff. As there is a maximum of one branch for each
member of staff involved in this relationship and a maximum of one member of
staff for each branch, we refer to this type of relationship as one-to-one, which we
usually abbreviate as (1:1).
Figure 12.14(b)
The multiplicity of
the Staff Manages
Branch one-to-one
(1:1) relationship.12.6
Structural Constraints
|
421
Diagrammatic representation of 1:1 relationships
An ER diagram of the Staff Manages Branch relationship is shown in Figure 12.14(b).
To represent that a member of staff can manage zero or one branch, we place a
“0..1” beside the Branch entity. To represent that a branch always has one manager,
we place a “1..1” beside the Staff entity. (Note that for a 1:1 relationship, we may
choose a relationship name that makes sense in either direction.)
12.6.2 One-to-Many (1:*) Relationships
Consider the relationship Oversees, which relates the Staff and PropertyForRent entity
types. Figure 12.15(a) displays three occurrences of the Staff Oversees PropertyForRent
relationship type (denoted rl, r2, and r3) using a semantic net. Each relationship
(rn) represents the association between a single Staff entity occurrence and a single
PropertyForRent entity occurrence. We represent each entity occurrence using the
values for the primary key attributes of the Staff and PropertyForRent entities, namely
staffNo and propertyNo.
Determining the multiplicity
In Figure 12.15(a) we see that staffNo SG37 oversees propertyNos PG21 and PG36,
and staffNo SA9 oversees propertyNo PA14 but staffNo SG5 does not oversee any prop-
erties for rent and propertyNo PG4 is not overseen by any member of staff. In sum-
mary, a member of staff can oversee zero or more properties for rent and a property
for rent is overseen by zero or one member of staff. Therefore, for members of staff
participating in this relationship there are many properties for rent, and for proper-
ties participating in this relationship there is a maximum of one member of staff. We
refer to this type of relationship as one-to-many, which we usually abbreviate as (1:*).
Diagrammatic representation of 1:* relationships An ER diagram of the Staff
Oversees PropertyForRent relationship is shown in Figure 12.15(b). To represent
that a member of staff can oversee zero or more properties for rent, we place a
“0..*” beside the PropertyForRent entity. To represent that each property for rent
is overseen by zero or one member of staff, we place a “0..1” beside the Staff entity.
(Note that with 1:* relationships, we choose a relationship name that makes sense
in the 1:* direction.)
Figure 12.15(a)
Semantic net
showing three
occurrences of
the Staff Oversees
PropertyForRent
relationship type.422
|
Chapter 12  Entity–Relationship Modeling
Figure 12.15(b)
The multiplicity of
the Staff Oversees
PropertyForRent
one-to-many (1:*)
relationship type.
If we know the actual minimum and maximum values for the multiplicity, we can
display these instead. For example, if a member of staff oversees a minimum of zero
and a maximum of 100 properties for rent, we can replace the “0..*” with “0..100.”
12.6.3 Many-to-Many (*:*) Relationships
Consider the relationship Advertises, which relates the Newspaper and PropertyForRent
entity types. Figure 12.16(a) displays four occurrences of the Advertises relation-
ship (denoted rl, r2, r3, and r4) using a semantic net. Each relationship (rn) rep-
resents the association between a single Newspaper entity occurrence and a single
PropertyForRent entity occurrence. We represent each entity occurrence using the
values for the primary key attributes of the Newspaper and PropertyForRent entity
types, namely newspaperName and propertyNo.
Determining the multiplicity
In Figure 12.16(a) we see that the Glasgow Daily advertises propertyNos PG21 and
PG36, The West News also advertises propertyNo PG36 and the Aberdeen Express
advertises propertyNo PA14. However, propertyNo PG4 is not advertised in any news-
paper. In other words, one newspaper advertises one or more properties for rent
and one property for rent is advertised in zero or more newspapers. Therefore, for
Figure 12.16(a)
Semantic net
showing four
occurrences of
the Newspaper
Advertises
PropertyForRent
relationship type.12.6
Structural Constraints
|
423
Figure 12.16(b)
The multiplicity of
the Newspaper
Advertises
PropertyForRent
many-to-many
(*:*) relationship.
newspapers there are many properties for rent, and for each property for rent par-
ticipating in this relationship there are many newspapers. We refer to this type of
relationship as many-to-many, which we usually abbreviate as (*:*).
Diagrammatic representation of *:* relationships
An ER diagram of the Newspaper Advertises PropertyForRent relationship is shown in
Figure 12.16(b). To represent that each newspaper can advertise one or more prop-
erties for rent, we place a “1..*” beside the PropertyForRent entity type. To represent
that each property for rent can be advertised by zero or more newspapers, we place a
“0..*” beside the Newspaper entity. (Note that for a *:* relationship, we may choose
a relationship name that makes sense in either direction.)
12.6.4 Multiplicity for Complex Relationships
Multiplicity for complex relationships—that is, those higher than binary—is slightly
more complex.
Multiplicity
(complex
­relationship)
The number (or range) of possible occurrences of an entity type in
an n-ary relationship when the other (n–1) values are fixed.
In general, the multiplicity for n-ary relationships represents the potential
number of entity occurrences in the relationship when (n–1) values are fixed for
the other participating entity types. For example, the multiplicity for a ternary
relationship represents the potential range of entity occurrences of a particular
entity in the relationship when the other two values representing the other two
entities are fixed. Consider the ternary Registers relationship between Staff, Branch,
and Client shown in Figure 12.7. Figure 12.17(a) displays five occurrences of the
Registers relationship (denoted rl to r5) using a semantic net. Each relationship
(rn) represents the association of a single Staff entity occurrence, a single Branch
entity occurrence, and a single Client entity occurrence. We represent each entity
occurrence using the values for the primary key attributes of the Staff, Branch, and
Client entities, namely staffNo, branchNo, and clientNo. In Figure 12.17(a) we exam-
ine the Registers relationship when the values for the Staff and Branch entities are
fixed.424
|
Chapter 12  Entity–Relationship Modeling
Figure 12.17(a)
Semantic net
showing five
occurrences of the
ternary Registers
relationship with
values for Staff and
Branch entity types
fixed.
Determining the multiplicity
In Figure 12.17(a) with the staffNo/branchNo values fixed there are zero or more clientNo
values. For example, staffNo SG37 at branchNo B003 registers clientNo CR56 and
CR74, and staffNo SG14 at branchNo B003 registers clientNo CR62, CR84, and CR91.
However, SG5 at branchNo B003 registers no clients. In other words, when the staffNo
and branchNo values are fixed the corresponding clientNo values are zero or more.
Therefore, the multiplicity of the Registers relationship from the perspective of the
Staff and Branch entities is 0..*, which is represented in the ER diagram by placing
the 0..* beside the Client entity.
If we repeat this test we find that the multiplicity when Staff/Client values are fixed
is 1..1, which is placed beside the Branch entity, and the Client/Branch values are fixed
is 1..1, which is placed beside the Staff entity. An ER diagram of the ternary Registers
relationship showing multiplicity is in Figure 12.17(b).
A summary of the possible ways that multiplicity constraints can be represented
along with a description of the meaning is shown in Table 12.1.
12.6.5 Cardinality and Participation Constraints
Multiplicity actually consists of two separate constraints known as cardinality and
participation.
Cardinality
Figure 12.17(b)
The multiplicity
of the ternary
Registers
relationship.
Describes the maximum number of possible relationship occur-
rences for an entity participating in a given relationship type.12.6
Table 12.1
Structural Constraints
|
425
A summary of ways to represent multiplicity constraints.
ALTERNATIVE WAYS TO REPRESENT
MULTIPLICITY CONSTRAINTSMEANING
0..1Zero or one entity occurrence
1..1 (or just 1)Exactly one entity occurrence
0..* (or just *)Zero or many entity occurrences
1..*One or many entity occurrences
5..10Minimum of 5 up to a maximum of 10 entity
occurrences
0, 3, 6–8Zero or three or six, seven, or eight entity
occurrences
The cardinality of a binary relationship is what we previously referred to as a one-
to-one (1:1), one-to-many (1:*), and many-to-many (*:*). The cardinality of a rela-
tionship appears as the maximum values for the multiplicity ranges on either side of
the relationship. For example, the Manages relationship shown in Figure 12.18 has
a one-to-one (1:1) cardinality, and this is represented by multiplicity ranges with a
maximum value of 1 on both sides of the relationship.
Participation
Determines whether all or only some entity occurrences partici-
pate in a relationship.
The participation constraint represents whether all entity occurrences are
involved in a particular relationship (referred to as mandatory participation) or
only some (referred to as optional participation). The participation of entities in a
Figure 12.18
Multiplicity
described as
cardinality and
participation
constraints for
the Staff Manages
Branch (1:1)
relationship.426
|
Chapter 12  Entity–Relationship Modeling
relationship appears as the minimum values for the multiplicity ranges on either side
of the relationship. Optional participation is represented as a minimum value of 0,
and mandatory participation is shown as a minimum value of 1. It is important to
note that the participation for a given entity in a relationship is represented by the
minimum value on the opposite side of the relationship; that is, the minimum value
for the multiplicity beside the related entity. For example, in Figure 12.18, the
optional participation for the Staff entity in the Manages relationship is shown as a
minimum value of 0 for the multiplicity beside the Branch entity and the mandatory
participation for the Branch entity in the Manages relationship is shown as a minimum
value of 1 for the multiplicity beside the Staff entity.
A summary of the conventions introduced in this section to represent the basic
concepts of the ER model is shown on the inside front cover of this book.''',
'''Data Administration and Database
­Administration
The Data Administration (DA) and Database Administrator (DBA) are responsible
for managing and controlling the activities associated with the corporate data and
the corporate database, respectively. The DA is more concerned with the early20.6
Data Administration and Database ­Administration
stages of the lifecycle, from planning through to logical database design. In con-
trast, the DBA is more concerned with the later stages, from application/physical
database design to operational maintenance. In this final section of the chapter,
we discuss the purpose and tasks associated with data and database administration.
20.6.1 Data Administration
Data
­administration
The management of the data resource, which includes database
planning, development, and maintenance of standards, policies
and procedures, and conceptual and logical database design.
The DA is responsible for the corporate data resource, which includes noncom-
puterized data, and in practice is often concerned with managing the shared data
of users or application areas of an organization. The DA has the primary respon-
sibility of consulting with and advising senior managers and ensuring that the
application of database technologies continues to support corporate objectives.
In some enterprises, data administration is a distinct functional area; in others
it may be combined with database administration. The tasks associated with data
administration are described in Table 20.3.
Table 20.3
Data administration tasks.
Selecting appropriate productivity tools.
Assisting in the development of the corporate IT/IS and enterprise strategies.
Undertaking feasibility studies and planning for database development.
Developing a corporate data model.
Determining the organization’s data requirements.
Setting data collection standards and establishing data formats.
Estimating volumes of data and likely growth.
Determining patterns and frequencies of data usage.
Determining data access requirements and safeguards for both legal and enterprise
requirements.
Undertaking conceptual and logical database design.
Liaising with database administration staff and application developers to ensure applications
meet all stated requirements.
Educating users on data standards and legal responsibilities.
Keeping up to date with IT/IS and enterprise developments.
Ensuring documentation is up to date and complete, including standards, policies, procedures,
use of the data dictionary, and controls on end-users.
Managing the data dictionary.
Liaising with users to determine new requirements and to resolve difficulties over data access
or performance.
Developing a security policy.
|
635636
|
Chapter 20   Security and Administration
Table 20.4
Database administration tasks.
Evaluating and selecting DBMS products.
Undertaking physical database design.
Implementing a physical database design using a target DBMS.
Defining security and integrity constraints.
Liaising with database application developers.
Developing test strategies.
Training users.
Responsible for “signing off” on the implemented database system.
Monitoring system performance and tuning the database as appropriate.
Performing backups routinely.
Ensuring that recovery mechanisms and procedures are in place.
Ensuring that documentation is complete, including in-house produced material.
Keeping up to date with software and hardware developments and costs, and installing updates
as necessary.
20.6.2 Database Administration
Database
administration
The management of the physical realization of a database
system, which includes physical database design and imple-
mentation, setting security and integrity controls, monitor-
ing system performance, and reorganizing the database, as
necessary.
The database administration staff are more technically oriented than the data
administration staff, requiring knowledge of specific DBMSs and the operating
system environment. Although the primary responsibilities are centered on devel-
oping and maintaining systems using the DBMS software to its fullest extent, DBA
staff also assist DA staff in other areas, as indicated in Table 20.4. The number of
staff assigned to the database administration functional area varies, and is often
determined by the size of the organization. The tasks of database administration
are described in Table 20.4.
20.6.3 Comparison of Data and Database Administration
The preceding sections examined the purpose and tasks associated with data
administration and database administration. In this final section we briefly contrast
these functional areas. Table 20.5 summarizes the main task differences of data
administration and database administration. Perhaps the most obvious difference
lies in the nature of the work carried out. Data administration staff tend to be
much more managerial, whereas the database administration staff tend to be more
technical.Chapter Summary
Table 20.5
|
637
Data administration and database administration—main task differences.
DATA ADMINISTRATIONDATABASE ADMINISTRATION
Involved in strategic IS planningEvaluates new DBMSs
Determines long-term goalsExecutes plans to achieve goals
Enforces standards, policies, and proceduresEnforces standards, policies, and procedures
Determines data requirementsImplements data requirements
Develops conceptual and logical database designDevelops logical and physical database design
Develops and maintains corporate data modelImplements physical database design
Coordinates system developmentMonitors and controls database
Managerial orientationTechnical orientation
DBMS-independentDBMS-dependent'''
]