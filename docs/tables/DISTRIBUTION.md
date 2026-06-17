# DISTRIBUTION

> Distribution is the parent table for distributions.

**Description:** Distribution  
**Table type:** ACTIVITY  
**Primary key:** `DISTRIBUTION_ID`  
**Columns:** 19  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ATTENTION` | VARCHAR(100) |  |  | Attention information. |
| 2 | `COMMIT_DT_TM` | DATETIME |  |  | Date & Time the distribution was committed. |
| 3 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time this row was created. |
| 5 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the insert of the row in the table. |
| 6 | `CREATE_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted the row. |
| 7 | `DISTRIBUTION_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 8 | `DISTRIBUTION_NBR` | VARCHAR(40) |  |  | The system assigned number that appears on the distribution. |
| 9 | `DISTRIBUTION_NBR_KEY` | VARCHAR(40) |  |  | The distribution_nbr field in all uppercase. |
| 10 | `FROM_LOCATION_CD` | DOUBLE | NOT NULL |  | The location that will be distributing the inventory. |
| 11 | `ISSUED_DT_TM` | DATETIME |  |  | The date and time the distribution was issued. |
| 12 | `OMF_SUCCESS_IND` | DOUBLE | NOT NULL |  | The value of 0 or 1 indicates the success or failure of the respective OMF table update. 1 indicates update to OMF table was successful and 0 indicates failure. |
| 13 | `STATUS_CD` | DOUBLE | NOT NULL |  | The status of the distribution. |
| 14 | `TO_LOCATION_CD` | DOUBLE | NOT NULL |  | The location which will be receiving the inventory. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [DIST_LINE_ITEM_R](DIST_LINE_ITEM_R.md) | `DISTRIBUTION_ID` |
| [DIST_REQ_R](DIST_REQ_R.md) | `DISTRIBUTION_ID` |
| [MM_TRANS_HEADER](MM_TRANS_HEADER.md) | `DISTRIBUTION_ID` |

