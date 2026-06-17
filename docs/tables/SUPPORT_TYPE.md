# SUPPORT_TYPE

> Table stores information about all the types of support provided by the grant sponsor organization

**Description:** Table stores all the types of support provided by the grant sponsor organization  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PROT_GRANT_SPONSOR_ID` | DOUBLE | NOT NULL | FK→ | FK to prot_grant_sponsor table .. identifies the sponsor |
| 2 | `SUPPORT_TYPE_CD` | DOUBLE | NOT NULL |  | The type of support provided by the grant sponsor - Code Set 17436 |
| 3 | `SUPPORT_TYPE_DESC_OTR` | VARCHAR(255) |  |  | Free text description of Other support provided by grant sponsor |
| 4 | `SUPPORT_TYPE_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PROT_GRANT_SPONSOR_ID` | [PROT_GRANT_SPONSOR](PROT_GRANT_SPONSOR.md) | `PROT_GRANT_SPONSOR_ID` |

