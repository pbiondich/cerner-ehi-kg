# PL_DEMOGRAPHICS

> This table the demographic elements to be displayed for each client.

**Description:** PL DEMOGRAPHICS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEMOGRAPHIC_CD` | DOUBLE | NOT NULL |  | Indicates the demographic element to be displayed for the associated client |
| 2 | `DEMO_SEQUENCE` | DOUBLE |  |  | Indicates the order inwhich this demographic element appears. |
| 3 | `DISPLAY_LABEL` | CHAR(30) |  |  | The display label for the demographic element. |
| 4 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Indicates the client that the demographic element should appear for in the demographics display |
| 5 | `PL_DEMOGRAPHICS_ID` | DOUBLE | NOT NULL |  | Unique identifier for the row. |
| 6 | `SEQUENCE` | DOUBLE |  |  | The order of the selected demographics. |
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

