# SUBSTANCE_PROPERTY

> Stores substance properties, such as attributes (ions) and intrinsics. Also stores atomic weights and valences.

**Description:** SUBSTANCE_PROPERTY  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PROPERTY_CD` | DOUBLE | NOT NULL |  | Code value for the property from code set 4700 |
| 2 | `PROPERTY_SOURCE_FLAG` | DOUBLE |  |  | 0 = System defined; 1 = User defined |
| 3 | `PROPERTY_TYPE_FLAG` | DOUBLE |  |  | An attribute is a property of an ingredient that can be used in an order. An intrinsic is a feature of an ingredient that can be reported based on the amount of the ingredient ordered, but cannot be used to order the ingredient. |
| 4 | `PROPERTY_WEIGHT` | DOUBLE | NOT NULL |  | Molar mass weight of the property. This weight is the sum of neutrons and protons in the nucleus of the atom |
| 5 | `SUBSTANCE_PROPERTY_ID` | DOUBLE | NOT NULL |  | Unique identifier of the property |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `VALENCE` | DOUBLE | NOT NULL |  | Valence of the property. In chemistry, valence is a number representing the capacity of a single atom or radical to combine with other atoms or radicals. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

