# CDI_WORK_QUEUE

> This table represents a CPDI Work Queue.

**Description:** CDI Work Queue  
**Table type:** REFERENCE  
**Primary key:** `CDI_WORK_QUEUE_ID`  
**Columns:** 14  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDI_WORK_QUEUE_ID` | DOUBLE | NOT NULL | PK | The unique primary key of this table. It is an internally generated number. |
| 2 | `DEFAULT_AUTHENTICATED_IND` | DOUBLE | NOT NULL |  | Specifies if clinical work items in this queue default to authenticated (1) or transcribed (0). |
| 3 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 4 | `PAGINATION_IND` | DOUBLE | NOT NULL |  | The column indicates whether or not the queue will utilize pagination of items within the queue when displayed in Work Queue Monitor. 0 indicates pagination is not active. 1 Indicates pagination is active. |
| 5 | `REG_ACTION_KEYS_TXT` | VARCHAR(2000) |  |  | Contains a list of values from RCA_REG_ACTION.REG_ACTION_KEY_TXT indicating the registration actions that can be performed within the context of this work queue. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `WORK_QUEUE_CD` | DOUBLE | NOT NULL |  | Code value for this work queue (used to associate work queue to other code value via the code_value_group table). |
| 12 | `WORK_QUEUE_DESCRIPTION` | VARCHAR(100) | NOT NULL |  | Description of the work queue. |
| 13 | `WORK_QUEUE_NAME` | VARCHAR(40) | NOT NULL |  | Name of the work queue. |
| 14 | `WORK_QUEUE_TYPE_CD` | DOUBLE | NOT NULL |  | Specifies the type of items that will be routed to this work queue. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [CDI_WORK_ITEM_ATTRIB_CNFG](CDI_WORK_ITEM_ATTRIB_CNFG.md) | `CDI_WORK_QUEUE_ID` |
| [CDI_WORK_QUEUE_ITEM_RELTN](CDI_WORK_QUEUE_ITEM_RELTN.md) | `CDI_WORK_QUEUE_ID` |
| [CDI_WORK_QUEUE_PRSNL_RELTN](CDI_WORK_QUEUE_PRSNL_RELTN.md) | `CDI_WORK_QUEUE_ID` |
| [CDI_WORK_QUEUE_TIME](CDI_WORK_QUEUE_TIME.md) | `CDI_WORK_QUEUE_ID` |

