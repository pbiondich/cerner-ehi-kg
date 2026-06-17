# EKS_DLG_EVENT

> Event tracking table, contains a row for each time an event has occurred

**Description:** EKS DLG EVENT  
**Table type:** ACTIVITY  
**Primary key:** `DLG_EVENT_ID`  
**Columns:** 24  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_FLAG` | DOUBLE |  |  | This flag indicates that an action may need to be taken on the incoming order.0 = Non-specified action.1 = Alert message display only. 2 = Cancel the triggering action. 3 = Continue the triggering action. 4 = Modify the triggering action.5 = Message from EKS_LOG_ACTION_A template. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `ALERT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Identifies an entry in the long text table which contains the free text associated with alert history. |
| 7 | `DLG_DT_TM` | DATETIME |  |  | The date and time when the triggered event occurred |
| 8 | `DLG_EVENT_ID` | DOUBLE | NOT NULL | PK | Sequence number which uniquely identifies the event |
| 9 | `DLG_NAME` | VARCHAR(255) |  | FK→ | Name of the Insight which executed. |
| 10 | `DLG_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the user who was logged in when the event or Insight executed. |
| 11 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 12 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Identifies entry in the long text table which contains the free text associated with override reasons. |
| 13 | `MODIFY_DLG_NAME` | VARCHAR(255) |  |  | Name of the trigger module or user defined name. |
| 14 | `OVERRIDE_DEFAULT_IND` | DOUBLE |  |  | Boolean to indicate whether the default Insights recommendation was overridden. True indicates default override |
| 15 | `OVERRIDE_REASON_CD` | DOUBLE | NOT NULL |  | Code value which indicates the user's reason for overriding the default action of an Insight |
| 16 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 17 | `TRIGGER_ENTITY_ID` | DOUBLE | NOT NULL |  | Identifier for the entity which triggered the event. Relates to the TRIGGER_ENTITY_NAME field |
| 18 | `TRIGGER_ENTITY_NAME` | CHAR(32) |  |  | Parent entity for the item which triggered this event. Relates to the TRIGGER_ENTITY_ID table. |
| 19 | `TRIGGER_ORDER_ID` | DOUBLE | NOT NULL |  | ID of trigger order drug. Not all rows on this table will have a value in column TRIGGER_ORDER_ID that exists in the PK column on the Orders table. Some times TRIGGER_ORDER_ID is getting populated with a generated order_id in cases where Orders invokes Discern alerts but a user then cancels the order based on the alert. When this happens there will be no matching PK in the Orders table. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ALERT_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `DLG_NAME` | [EKS_DLG](EKS_DLG.md) | `DLG_NAME` |
| `DLG_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [EKS_DLG_EVENT_ATTR](EKS_DLG_EVENT_ATTR.md) | `DLG_EVENT_ID` |

