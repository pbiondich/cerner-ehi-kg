# ESO_TRIGGER

> This table defines the event triggers for the ESO Server to process. The element on this table illustrates how to identify each trigger. The active indicator on this table defines whether the trigger is configured for outbound processing.

**Description:** ESO Trigger Table  
**Table type:** REFERENCE  
**Primary key:** `TRIGGER_ID`  
**Columns:** 23  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CALL_SRV_FLAG` | DOUBLE |  |  | This table row is 1 or 0. It either call the eso server or it doesn't |
| 3 | `CLASS` | VARCHAR(15) |  |  | Identifies the ESO server processing class of the transaction. |
| 4 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | This is the date and time that a row is created in the eso_trigger table. |
| 5 | `DESCRIPTION` | VARCHAR(256) |  |  | This string provides a description of the event trigger row. |
| 6 | `INTERFACE_TYPE_CD` | DOUBLE | NOT NULL |  | This field creates at relation from the particular ESO trigger combination to a interface type. Multiple ESO triggers can be associated to a single interface type. |
| 7 | `MESSAGE_FORMAT_CD` | DOUBLE | NOT NULL |  | Format of the message |
| 8 | `MESSAGE_TRIGGER_CD` | DOUBLE | NOT NULL |  | message trigger codeColumn |
| 9 | `MESSAGE_TYPE_CD` | DOUBLE | NOT NULL |  | Type of the message |
| 10 | `MESSAGE_VERSION_CD` | DOUBLE | NOT NULL |  | Version of the message |
| 11 | `PROCESSING_CONTROL` | DOUBLE |  |  | This number controls specific ESO server processing method when executing the trigger event. |
| 12 | `REQUEST_NBR` | DOUBLE | NOT NULL |  | Ddefines the TDB request number for the HL7 csa objects. |
| 13 | `SCP_BINDING` | VARCHAR(128) |  |  | Identifies the ESO server processing scp binding of the transaction. |
| 14 | `SOURCE_REQ_NBR` | DOUBLE |  |  | For X12 transactions, it provides the TDB request number. |
| 15 | `SUBTYPE` | VARCHAR(15) |  |  | Identifies the ESO server processing subtype of the transaction. |
| 16 | `SUBTYPE_DETAIL` | VARCHAR(15) |  |  | Identifies the ESO server processing subtype detail of the transaction. |
| 17 | `TRIGGER_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the eso_trigger table. It is an internal system assigned number. |
| 18 | `TYPE` | VARCHAR(15) |  |  | Identifies the ESO server processing type of the transaction. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (4)

| From table | Column |
|------------|--------|
| [CHART_REQUEST](CHART_REQUEST.md) | `TRIGGER_ID` |
| [CQM_FSIESO_TR_1](CQM_FSIESO_TR_1.md) | `ESO_TRIGGER_ID` |
| [ESO_TRIG_ROUTINE_R](ESO_TRIG_ROUTINE_R.md) | `TRIGGER_ID` |
| [SI_ESO_TRIGGER_HIST](SI_ESO_TRIGGER_HIST.md) | `TRIGGER_ID` |

