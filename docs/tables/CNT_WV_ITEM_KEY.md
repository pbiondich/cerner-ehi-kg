# CNT_WV_ITEM_KEY

> Contains details about working view items which are used by Bedrock tool. Imported using content manager tool.

**Description:** Content Working View Item Key  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CNT_WV_ITEM_KEY_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CNT_WV_ITEM_KEY table. |
| 2 | `DCP_WV_ITEM_REF_ID` | DOUBLE |  | FK→ | When the configuration is imported from from .xml/.czf to this table, ithis column will be populated with a null value. When Bedrock tool maps this record, it will be updated to the parent row from WORKING_VIEW_ITEM. |
| 3 | `DISP_ASSOC_IND` | DOUBLE | NOT NULL |  | Working view display association indicator |
| 4 | `FALLOFF_VIEW_MINUTES` | DOUBLE | NOT NULL |  | Specifies when to remove the item if it hasn't been documented on within the working view |
| 5 | `INCLUDED_IND` | DOUBLE | NOT NULL |  | Specifies whether the event set is included on the working view. |
| 6 | `PARENT_EVENT_SET_NAME` | VARCHAR(40) | NOT NULL |  | Specifies the primitive event set parents associated to a working view section. |
| 7 | `PRIMITIVE_EVENT_SET_NAME` | VARCHAR(40) | NOT NULL |  | Specifies the primitive event sets associated to a working view section. |
| 8 | `TASK_ASSAY_GUID` | VARCHAR(100) |  |  | GUID - used to link between item and DTA |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The date of the version for the given data |
| 15 | `WV_ITEM_UID` | VARCHAR(100) | NOT NULL |  | UID(unique identification) number which is used in versioning of working view section in conjunction with version_dt_tm column |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DCP_WV_ITEM_REF_ID` | [WORKING_VIEW_ITEM](WORKING_VIEW_ITEM.md) | `WORKING_VIEW_ITEM_ID` |

