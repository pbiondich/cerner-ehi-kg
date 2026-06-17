# CREG_SPECIFICITY

> Defines the HLA specificities included in a particular cross reactive group (CREG).

**Description:** CREG Specificity  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREG_ID` | DOUBLE | NOT NULL | FK→ | Relates the specificity to a specific Cross Reactive Group (CREG). It is a foreign key reference to the primary key of the CREG table. |
| 2 | `CREG_SEQUENCE` | DOUBLE | NOT NULL |  | Arbitrarily assigned number to make each record unique. This is necessary since HLA Type is not numeric and therefore cannot be part of the primary key. |
| 3 | `HLA_TYPE` | VARCHAR(20) |  |  | An HLA specificity contained within the CREG. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREG_ID` | [CREG](CREG.md) | `CREG_ID` |

