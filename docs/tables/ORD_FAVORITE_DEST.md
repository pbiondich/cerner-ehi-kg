# ORD_FAVORITE_DEST

> User's favorite output destination for prescriptions.

**Description:** Order Favorite Destination  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEST_TXT` | VARCHAR(100) |  |  | Textual information of ad hoc destination |
| 2 | `FAVORITE_DEST_SEQ` | DOUBLE | NOT NULL |  | Sequencing of multiple output destinations of a person. |
| 3 | `ORD_FAVORITE_DEST_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a user's favorite output destination for prescriptions. |
| 4 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The organization that the output dest belongs. |
| 5 | `OUTPUT_DEST_ID` | DOUBLE | NOT NULL | FK→ | Identifies the output destination |
| 6 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the personnel associated to the established favorite output destination. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `OUTPUT_DEST_ID` | [OUTPUT_DEST](OUTPUT_DEST.md) | `OUTPUT_DEST_CD` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

