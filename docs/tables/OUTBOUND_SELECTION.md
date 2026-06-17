# OUTBOUND_SELECTION

> Defines the selection criteria for outbound transaction from HNA Millenium

**Description:** ESO Outbound Selection Table  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 31

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | Send transaction based upon order action type (i.e. New Order, Complete, ...) |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | Send transactions based upon order activity type |
| 7 | `AFTER_DISCHARGE_IND` | DOUBLE |  |  | Send transaction based upon patient discharge, the NUMBER_OF_DAYS element should be used to specify the days after discharge |
| 8 | `ALIAS_POOL_CD` | DOUBLE | NOT NULL |  | Alias pool code identifies a unique set or list of identifiers (I.e., numbers). The alias pool code also determines the accept/display format for the unique set of identifiers. |
| 9 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 10 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 11 | `CS_FLAG` | DOUBLE |  |  | Order Management Careset Flag |
| 12 | `DEPT_ORDER_STATUS_CD` | DOUBLE | NOT NULL |  | Send transaction based upon the department status of the order. |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `FROM_CONTRIB_SYS_CD` | DOUBLE | NOT NULL |  | Send transactions based upon the "FROM" sending contributor system. This field is typically associated with order transaction. |
| 15 | `HL7_EVENT_CD` | DOUBLE | NOT NULL |  | Send transactions based upon the HL7 trigger event code. Examples are A01, A02, ALL ADTS, etc. |
| 16 | `HL7_ORDER_CTRL_CD` | DOUBLE | NOT NULL |  | Send Order Transactions based upon the HL7 Order Control Mnemonic. |
| 17 | `NUMBER_OF_DAYS` | DOUBLE |  |  | When the AFTER_DISCHARGE_IND is set, this send transactions if the number of days after discharge of the patient meets or exceeds this number |
| 18 | `ORDERABLE_TYPE_FLAG` | DOUBLE |  |  | Order Management Orderable Type Flag. |
| 19 | `ORDER_STATUS_CD` | DOUBLE | NOT NULL |  | Send transaction based upon the order status. |
| 20 | `ORDER_TEMPLATE_FLAG` | DOUBLE |  |  | Send transaction based upon whether the order is part os a template |
| 21 | `ORGANIZTION_ID` | DOUBLE | NOT NULL |  | Send transaction based upon organization Id. This is the value of the unique primary identifier of the organization table. It is an internal system assigned number. |
| 22 | `PATIENT_TYPE_CD` | DOUBLE | NOT NULL |  | Send transaction based upon patient type. Encounter type is synonymous with patient type. Encounter type is used to categorize patients into inpatient and outpatient groups. |
| 23 | `PROCESSING_CD` | DOUBLE | NOT NULL |  | This field identifies the processing method for each row. The typical configuration will identify whether to send or don't send. |
| 24 | `SELECTION_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the selection criteria for the DB row. This is part of the unique identifier for this table. |
| 25 | `SEQ_NUM` | DOUBLE | NOT NULL |  | Defines the sequence number in the table. |
| 26 | `TO_CONTRIB_SYS_CD` | DOUBLE | NOT NULL |  | Send transactions based upon the "TO" sending contributor system. This field is typically associated with order transaction. |
| 27 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 28 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 29 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 30 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 31 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

