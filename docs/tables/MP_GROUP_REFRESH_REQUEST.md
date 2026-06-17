# MP_GROUP_REFRESH_REQUEST

> An activity table containing all of the refresh requests of the MPages Static Content Server.

**Description:** MP GROUP REFRESH REQUEST  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BASE_FOLDER` | VARCHAR(255) | NOT NULL |  | The folder that will be refreshed. |
| 2 | `BASE_URL` | VARCHAR(200) | NOT NULL |  | An identifier for the WebSphere cluster on which the application is deployed. |
| 3 | `MP_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key value from the MP_GROUP table.The group id of the folder that will be refreshed - or 0 if the folder is specified in environment entries. |
| 4 | `MP_GROUP_REFRESH_REQUEST_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 5 | `REQUEST_DT_TM` | DATETIME | NOT NULL |  | The date and time that the cached folder refresh request was created. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MP_GROUP_ID` | [MP_GROUP](MP_GROUP.md) | `MP_GROUP_ID` |

