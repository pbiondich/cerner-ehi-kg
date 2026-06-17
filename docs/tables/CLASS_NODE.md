# CLASS_NODE

> An individual class node in the classfication (eg. Sutures).

**Description:** Classification Node.  
**Table type:** REFERENCE  
**Primary key:** `CLASS_NODE_ID`  
**Columns:** 19  
**Referenced by:** 18 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CLASS_INSTANCE_CD` | DOUBLE | NOT NULL |  | The classification instance which this node is built under. |
| 6 | `CLASS_NODE_ID` | DOUBLE | NOT NULL | PK | Primary key |
| 7 | `CLASS_TYPE_CD` | DOUBLE | NOT NULL |  | The type of classification the being defined (e.g. Item Class, Ordering Class, Reporting Class). |
| 8 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 9 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the row was inserted. |
| 10 | `CREATE_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the insert of the row in the table. |
| 11 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted the row. |
| 12 | `DESCRIPTION` | VARCHAR(60) |  |  | Description of the class node. |
| 13 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 14 | `SHORT_DESCRIPTION` | VARCHAR(40) |  |  | Short description of the class node. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (18)

| From table | Column |
|------------|--------|
| [CLASS_GROUP](CLASS_GROUP.md) | `CHILD_CLASS_NODE_ID` |
| [CLASS_GROUP](CLASS_GROUP.md) | `PARENT_CLASS_NODE_ID` |
| [ITEM_CLASS_NODE_R](ITEM_CLASS_NODE_R.md) | `CLASS_NODE_ID` |
| [MM_APPROVAL](MM_APPROVAL.md) | `CLASS_NODE_ID` |
| [MM_APPROVAL_QUEUE](MM_APPROVAL_QUEUE.md) | `CLASS_NODE_ID` |
| [MM_CYCLE_CNT_FILTER](MM_CYCLE_CNT_FILTER.md) | `CLASS_NODE_ID` |
| [MM_OMF_ITEM_MASTER](MM_OMF_ITEM_MASTER.md) | `CLASS_NODE_ID` |
| [MM_PRICE_FORMULA_CLASS_R](MM_PRICE_FORMULA_CLASS_R.md) | `CLASS_NODE_ID` |
| [MM_REQ_FILL_ROUTE](MM_REQ_FILL_ROUTE.md) | `CLASS_NODE_ID` |
| [MM_SUPPLY_CABINET](MM_SUPPLY_CABINET.md) | `ITEM_CLASS_ID` |
| [MM_XFI_CNTRCT_HDR](MM_XFI_CNTRCT_HDR.md) | `CLASS_NODE_ID` |
| [MM_XFI_CNTRCT_HDR_TIER](MM_XFI_CNTRCT_HDR_TIER.md) | `CLASS_NODE_ID` |
| [MM_XFI_CNTRCT_PRICE_ADJ](MM_XFI_CNTRCT_PRICE_ADJ.md) | `ADJ_CLASS_NODE_ID` |
| [MM_XFI_ITEM](MM_XFI_ITEM.md) | `CLASS_NODE_ID` |
| [OBJECT_IDENTIFIER_INDEX](OBJECT_IDENTIFIER_INDEX.md) | `OBJECT_PARENT_NODE_ID` |
| [PRSNL_CLASS_NODE_R](PRSNL_CLASS_NODE_R.md) | `CLASS_NODE_ID` |
| [SEGMENT_REFERENCE](SEGMENT_REFERENCE.md) | `EQUIP_CLASS_NODE_ID` |
| [SN_SUP_CAB_PREF_CLASS](SN_SUP_CAB_PREF_CLASS.md) | `ITEM_CLASS_ID` |

