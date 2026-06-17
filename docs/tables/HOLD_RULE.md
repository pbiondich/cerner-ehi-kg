# HOLD_RULE

> The table identifies the events that eligable or not eligable for hold and the hold processing rules associated with those events.

**Description:** Hold Rule  
**Table type:** REFERENCE  
**Primary key:** `HOLD_RULE_ID`  
**Columns:** 24  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_CONTRIB_SYS_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | A grouping mechanism within catalog type code. |
| 4 | `CATALOG_CD` | DOUBLE | NOT NULL |  | Coded value which specifies how the event is stored in and retrieved from the event table's sub-tables. For example, Catalog_CDs identify events as numeric results, textual results, calculations, medications, etc. |
| 5 | `CLASS` | VARCHAR(15) |  |  | Identifies the ESO server processing class of the transaction. |
| 6 | `DESCRIPTION` | VARCHAR(30) |  |  | This fields allows the User to customize the identification of the particular hold rule row. |
| 7 | `ENCNTR_FIRST_EVENT_FLAG` | DOUBLE | NOT NULL |  | This element masks for PM outbound events that specify encntr_first_event_ind. Typically ADT events with A01, A04, or A05 types may utilize this mask. |
| 8 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | Encounter type is used to categorize patients into inpatient and outpatient groups. |
| 9 | `EVENT_CD` | DOUBLE | NOT NULL |  | Coded value which specifies how the event is stored in and retrieved from the event table's sub-tables. For example, Event_CDs identify events as numeric results, textual results, calculations, medications, etc. |
| 10 | `EVENT_CLASS_CD` | DOUBLE | NOT NULL |  | Coded value which specifies how the event is stored in and retrieved from the event table's sub-tables. For example, Event_Class_CDs identify events as numeric results, textual results, calculations, medications, etc. |
| 11 | `HOLD_RULE_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 12 | `INTERFACE_TYPE_CD` | DOUBLE | NOT NULL |  | This field creates at relation from the particular ESO trigger combination to a interface type. Multiple ESO triggers can be associated to a single interface type. |
| 13 | `MESSAGE_VERSION_CD` | DOUBLE | NOT NULL |  | Version of the message |
| 14 | `ORDER_ACTION_CD` | DOUBLE | NOT NULL |  | Code value to identify the action that was performed. |
| 15 | `ORGANIZATION_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the organization table. It is an internal system assigned number. |
| 16 | `PERSON_FIRST_EVENT_FLAG` | DOUBLE | NOT NULL |  | This element masks for PM outbound events that specify personr_first_event_ind. Typically ADT events with A01, A04, A05, or A28 types may utilize this mask. |
| 17 | `RULE_ACTION_CD` | DOUBLE | NOT NULL |  | This element specifies the processing rules to follow when the hold_rule identifies matches an outbound event. |
| 18 | `SUBTYPE` | VARCHAR(15) |  |  | Identifies the ESO server processing subtype of the transaction. |
| 19 | `TYPE` | VARCHAR(15) |  |  | Identifies the ESO server processing type of the transaction. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [HOLD_QUEUE](HOLD_QUEUE.md) | `HOLD_RULE_ID` |
| [HOLD_RULE_CONDITION](HOLD_RULE_CONDITION.md) | `HOLD_RULE_ID` |

