# CDI_WORK_ITEM

> This table represents a CPDI Work Item within the routing and queuing process.

**Description:** CDI Work Item  
**Table type:** ACTIVITY  
**Primary key:** `CDI_WORK_ITEM_ID`  
**Columns:** 21  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTO_DIAL_IND` | DOUBLE | NOT NULL |  | Indicates whether or not this workitem is an auto dial. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CATEGORY_CD` | DOUBLE | NOT NULL |  | The generic category of the work item. Category is a generic concept that allows clients to define their own list of descriptors for a work item. Clients might have their own configurable codeset so it is documented as 0, |
| 4 | `CDI_WORK_ITEM_ID` | DOUBLE | NOT NULL | PK | The unique primary key of this table. It is internally assigned. |
| 5 | `CLARIFY_REASON_CD` | DOUBLE | NOT NULL |  | The code value for the reason the work item was put in a clarify status. |
| 6 | `COMMENT_ID` | DOUBLE | NOT NULL | FK→ | The link to the row on the long_text table which includes comments associated to the image. |
| 7 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the work item was added into the system. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `ORDERING_PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | Person ID from the PRSNL table. |
| 10 | `OWNER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel identifier for the person who has ownership of the work item. If valued, this field means this person has the work item locked. |
| 11 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | This field contains the identifier for the parent table row. |
| 12 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | This field contains the name of table that this cdi_work_item row is associated to. |
| 13 | `PREV_CDI_WORK_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Identifier of the currently effective row based off the begin/end effective date/time values |
| 14 | `PRIORITY_CD` | DOUBLE | NOT NULL |  | The priority of the work item. |
| 15 | `SCH_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the requested/scheduled appointment. |
| 16 | `STATUS_CD` | DOUBLE | NOT NULL |  | The status of the work item. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ORDERING_PROVIDER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `OWNER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PREV_CDI_WORK_ITEM_ID` | [CDI_WORK_ITEM](CDI_WORK_ITEM.md) | `CDI_WORK_ITEM_ID` |
| `SCH_EVENT_ID` | [SCH_EVENT](SCH_EVENT.md) | `SCH_EVENT_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [CDI_WORK_ITEM](CDI_WORK_ITEM.md) | `PREV_CDI_WORK_ITEM_ID` |
| [CDI_WORK_ITEM_ACTION](CDI_WORK_ITEM_ACTION.md) | `CDI_WORK_ITEM_ID` |
| [CDI_WORK_ITEM_ATTRIBUTE](CDI_WORK_ITEM_ATTRIBUTE.md) | `CDI_WORK_ITEM_ID` |
| [CDI_WORK_QUEUE_ITEM_RELTN](CDI_WORK_QUEUE_ITEM_RELTN.md) | `CDI_WORK_ITEM_ID` |

