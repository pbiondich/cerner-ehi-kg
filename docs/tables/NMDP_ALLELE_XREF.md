# NMDP_ALLELE_XREF

> Cross Reference table that relates generated NMDP Codes to the Allele Cd's that make up the NMDP Code group.

**Description:** NMDP Allele XRef  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALLELE_CD` | DOUBLE | NOT NULL |  | Code Value for the Allele that makes up part of the NMDP Code generated. |
| 2 | `NMDP_CD` | DOUBLE | NOT NULL |  | Code Value for the NMDP code that was generated for a specific set of alleles. |
| 3 | `NMDP_CODE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key reference to the generated NMDP Code for the list of Alleles that are contained within the code. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NMDP_CODE_ID` | [NMDP_CODE](NMDP_CODE.md) | `NMDP_CODE_ID` |

