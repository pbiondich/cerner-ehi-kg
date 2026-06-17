# REQUEST_PROCESSING

> This is the configuration table for the Process Server. It determines based on inbound request number, what processing should occur when that request is received.

**Description:** Process Server Request Process Configuration  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DESTINATION_STEP_ID` | DOUBLE | NOT NULL |  | This is the ID of the destination of the request through the process server |
| 3 | `FORMAT_SCRIPT` | VARCHAR(30) |  |  | This is the script that formats the request before being set to the process server. This is the script that will executed in order to format the data from the in bound request into the form of the out bound request. This script must be named PFMT_*. |
| 4 | `FORWARD_OVERRIDE_IND` | DOUBLE |  |  | This indicator will allow the request to the destination server to be forwarded back to the process server. In most cases this indicator will not be checked, because this scenario would have the characteristics of a loop. But if there is some condition that the destination needs to send back to the process server this indicator should be checked. |
| 5 | `REPROCESS_REPLY_IND` | DOUBLE |  |  | This field determines if the reply from the server perform should be processed. A value of 1 indicates it should, a value of 0 indicates it should not. The following rules apply to processing THE reply from servers in this manner. 1.The server has to be a RR (Request/Reply) type server. 2.The script handler will be named the same as the format script name with "_EPI" appended to the end of the name. 3.The data structures that are exposed are as follows The request and reply of the original |
| 6 | `REQUEST_NUMBER` | DOUBLE | NOT NULL | FK→ | This is the unique request structure that the processes are being added to. |
| 7 | `SEQUENCE` | DOUBLE | NOT NULL |  | This is the number that identifies which order in the process a request will be executed. |
| 8 | `SERVICE` | VARCHAR(50) |  |  | This is will override the default service of the destination step. The destination could offer more that one service depending on the parameters being passed. |
| 9 | `TARGET_REQUEST_NUMBER` | DOUBLE |  |  | This is the number of a process in the processing chain for the request. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REQUEST_NUMBER` | [REQUEST](REQUEST.md) | `REQUEST_NUMBER` |

