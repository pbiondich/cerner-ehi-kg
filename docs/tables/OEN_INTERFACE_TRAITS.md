# OEN_INTERFACE_TRAITS

> OEN interface traits

**Description:** Contains traits for interface  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `INTERFACE_ID` | DOUBLE | NOT NULL | FK→ | interface idColumn |
| 3 | `NAME` | VARCHAR(32) | NOT NULL |  | Name of the trait |
| 4 | `SEQUENCE_NBR` | DOUBLE | NOT NULL |  | This column determine which version interface trait is it? |
| 5 | `TRAIT_ID` | DOUBLE | NOT NULL |  | Id of the trait. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `VALUE_IND` | DOUBLE |  |  | If trait is Boolean type then 0 represents FALSE and 1 represents TRUE. |
| 12 | `VALUE_INT` | DOUBLE |  |  | If trait is integer type, then this field indicates trait's integer value. |
| 13 | `VALUE_TEXT` | VARCHAR(255) |  |  | if trait is of type text, then this field is filled with the trait value. |
| 14 | `VERSION_NBR` | DOUBLE | NOT NULL |  | Version of the trait. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INTERFACE_ID` | [OEN_INTERFACE](OEN_INTERFACE.md) | `INTERFACE_ID` |

