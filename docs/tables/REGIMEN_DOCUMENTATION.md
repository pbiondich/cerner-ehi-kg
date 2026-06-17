# REGIMEN_DOCUMENTATION

> Holds responses at the regimen or regimen detail level.

**Description:** REGIMEN DOCUMENTATION  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CHART_DT_TM` | DATETIME | NOT NULL |  | Date & time the regimen response was charted |
| 3 | `CHART_PRSNL_ID` | DOUBLE | NOT NULL |  | unique identifier of the person who documented the response |
| 4 | `CHART_TZ` | DOUBLE | NOT NULL |  | Time zone associated with the corresponding dt_tm column. |
| 5 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | Free text Patient's response to treatment or regimen comment |
| 6 | `REGIMEN_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | sequence name: CareNet_seq Unique identifier for the REGIMEN _DETAIL table. |
| 7 | `REGIMEN_DOCUMENTATION_ID` | DOUBLE | NOT NULL |  | sequence name: CareNet_seq Unique identifier for the REGIMEN _DOCUMENTATION table. |
| 8 | `REGIMEN_ID` | DOUBLE | NOT NULL | FK→ | sequence name: CareNet_seq Unique identifier for the REGIMEN table. |
| 9 | `RESPONSE_CD` | DOUBLE | NOT NULL |  | Codified Patient's response to treatment |
| 10 | `TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates a type of documentation. 1-Patient's response to treatment 2-Regimen comment |
| 11 | `UNCHART_DT_TM` | DATETIME |  |  | Date & time the regimen response was uncharted |
| 12 | `UNCHART_PRSNL_ID` | DOUBLE | NOT NULL |  | unique identifier of the person who removed the documented response |
| 13 | `UNCHART_TZ` | DOUBLE | NOT NULL |  | Time zone associated with the corresponding dt_tm column. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REGIMEN_DETAIL_ID` | [REGIMEN_DETAIL](REGIMEN_DETAIL.md) | `REGIMEN_DETAIL_ID` |
| `REGIMEN_ID` | [REGIMEN](REGIMEN.md) | `REGIMEN_ID` |

