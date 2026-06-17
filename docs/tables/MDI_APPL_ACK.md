# MDI_APPL_ACK

> An Activity table which tracks the status and requests for MDI Application Acknowledgements.

**Description:** MDI Application Acknowledgement  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION` | VARCHAR(20) |  |  | Identifies the accession number from the PROP_ORDER table when a request is successful. |
| 2 | `CREATE_DT_TM` | DATETIME |  |  | Date row was created. |
| 3 | `ERROR_COND` | VARCHAR(4) |  |  | A four digit error number that uniquely identifies the error when a request fails to place an order or post results. |
| 4 | `INPROCESS_IND` | DOUBLE |  |  | Indicates if this request is currently being processed. |
| 5 | `MESSAGE_IDENT` | VARCHAR(32) |  |  | A string received via a HL7 version 2.4 interface in the MSH segment, sequence 10. Used to uniquely identify HL7 messages. |
| 6 | `ORDER_ID` | DOUBLE | NOT NULL |  | Order ID to which this transfer record is associated. |
| 7 | `PROCESS_STATUS_FLAG` | DOUBLE |  |  | A two digit value that represents the status of requests in this table. |
| 8 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | Identifies which service resource sent this request. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SERVICE_RESOURCE_CD` | [LAB_INSTRUMENT](LAB_INSTRUMENT.md) | `SERVICE_RESOURCE_CD` |

