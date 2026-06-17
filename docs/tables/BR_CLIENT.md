# BR_CLIENT

> stores all bedrock clients

**Description:** BEDROCK CLIENT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AUTOBUILD_CLIENT_ID` | DOUBLE | NOT NULL |  | indicates which autobuild should be used |
| 6 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 7 | `BR_CLIENT_NAME` | VARCHAR(255) | NOT NULL |  | name of bedrock client |
| 8 | `CLIENT_MNEMONIC` | VARCHAR(12) |  |  | client's Cerner mnemonic |
| 9 | `DATA_MOVE_READY_IND` | DOUBLE |  |  | indicates if the client's data is ready to move |
| 10 | `FRANCHISE_CLIENT_ID` | DOUBLE | NOT NULL |  | Holds the client_id of the parent if the client is a franchise child |
| 11 | `FRANCHISE_FLAG` | DOUBLE | NOT NULL |  | Determines whether the client is a franchise parent or child. A value of 1 means the client is a franchise parent, a value of 2 means the client is a child of a franchise parent |
| 12 | `OPERATING_SYSTEM` | VARCHAR(3) |  |  | operating system of the Millennium database |
| 13 | `REGION` | VARCHAR(100) | NOT NULL |  | country the client is in |
| 14 | `SITE_READY_IND` | DOUBLE | NOT NULL |  | indicates if the site is ready to start |
| 15 | `START_VERSION_NBR` | DOUBLE | NOT NULL |  | Identifies which version of start has been loaded |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

