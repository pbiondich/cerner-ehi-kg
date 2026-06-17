# SN_RPT_GRP_R

> This is a relationship table for the reports and the report groups in SurgiNet.

**Description:** SN RPT GRP R  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 2 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the row was first inserted. |
| 3 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the row to be created in the table. |
| 4 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted the row. |
| 5 | `ORDER_SEQ` | DOUBLE | NOT NULL |  | The sequence of the report in the group. |
| 6 | `RPT_GRP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key into the SN_RPT_GRP table to determine the group that this relationship goes with. |
| 7 | `RPT_GRP_R_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 8 | `RPT_ID` | DOUBLE | NOT NULL |  | Foreign key into the SN_RPT table to determine which report this relationship goes with. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RPT_GRP_ID` | [SN_RPT_GRP](SN_RPT_GRP.md) | `RPT_GRP_ID` |

