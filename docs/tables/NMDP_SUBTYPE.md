# NMDP_SUBTYPE

> Defines the various allele subtypes that make up an NMDP Code group.

**Description:** NMDP Subtype  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `NMDP_SUFFIX_ID` | DOUBLE | NOT NULL | FK→ | Relates the subtype to a specific NMDP Suffix. It is a foreign key reference to the primary key of the NMDP_SUFFIX table. |
| 2 | `SUBTYPE_DESC` | VARCHAR(255) |  |  | The allele subtype that is part of the NMDP Code group. |
| 3 | `SUBTYPE_SEQUENCE` | DOUBLE | NOT NULL |  | Arbitrarily assigned number to make each record unique. This is necessary since Subtype Description is not numeric and therefore cannot be part of the primary key. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NMDP_SUFFIX_ID` | [NMDP_SUFFIX](NMDP_SUFFIX.md) | `NMDP_SUFFIX_ID` |

