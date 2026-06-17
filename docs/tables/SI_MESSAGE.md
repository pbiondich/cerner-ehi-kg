# SI_MESSAGE

> This table defines an inbound message

**Description:** SI MESSAGE  
**Table type:** REFERENCE  
**Primary key:** `MESSAGE_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `APPLICATION` | VARCHAR(10) | NOT NULL |  | This indicates the ownership of the row.Column |
| 3 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | This is the Date & Time the row was created.Column |
| 4 | `INTERFACE_TYPE_CD` | DOUBLE | NOT NULL |  | Interface type code. Defines what kind of interface. |
| 5 | `MAP_NBR` | DOUBLE | NOT NULL |  | This is the TDB number of the proprietary object the inbound message will be mapped into |
| 6 | `MESSAGE_DESC` | VARCHAR(255) | NOT NULL |  | Simply a description of the message.Column |
| 7 | `MESSAGE_FORMAT_CD` | DOUBLE | NOT NULL |  | This is used to identify what format the messages are in.Column |
| 8 | `MESSAGE_ID` | DOUBLE | NOT NULL | PK | This uniquely identifies a message with an application.Column |
| 9 | `MESSAGE_TRIGGER_CD` | DOUBLE | NOT NULL |  | This identifies the Trigger Type of the message (ex. A01).Column |
| 10 | `MESSAGE_TYPE_CD` | DOUBLE | NOT NULL |  | This identifies the type of message (ex. ADT, ORU etc.).Column |
| 11 | `MESSAGE_VERSION_CD` | DOUBLE | NOT NULL |  | This identifies the version of the message (ex. 2.3, 4010 etc.).Column |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SI_COMSRV_MSG_MAP_R](SI_COMSRV_MSG_MAP_R.md) | `MESSAGE_ID` |

