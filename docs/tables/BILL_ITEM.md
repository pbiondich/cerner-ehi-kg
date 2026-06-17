# BILL_ITEM

> Contains all items/activities that can be billed for.

**Description:** Bill Item.  
**Table type:** REFERENCE  
**Primary key:** `BILL_ITEM_ID`  
**Columns:** 38  
**Referenced by:** 17 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BILL_ITEM_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the bill item ..... |
| 7 | `CALC_TYPE_CD` | DOUBLE | NOT NULL |  | not used |
| 8 | `CARESET_IND` | DOUBLE |  |  | Identifies a bill item as a careset (an orderable is a group of other orderables and/or tasks). |
| 9 | `CHARGE_POINT_CD` | DOUBLE | NOT NULL |  | not used |
| 10 | `CHILD_SEQ` | DOUBLE |  |  | The child sequence is used for caresets only, to allow an orderable to be added into a careset multiple times. |
| 11 | `COST_BASIS_AMT` | DOUBLE | NOT NULL |  | This is the cost on which the final charge price is based on (before markups, discounts, tax, etc.) |
| 12 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 13 | `EXT_CHILD_CONTRIBUTOR_CD` | DOUBLE | NOT NULL |  | Value from 13016 that represents the source of the child bill item. It makes the child reference id unique (in the case of multiple child reference id sources) |
| 14 | `EXT_CHILD_ENTITY_NAME` | VARCHAR(32) |  |  | Indicates whether the contributor was another bill item as in the case of specific addons as indicated by 'bill_item', or if it was an external contributor as indicated by 'code_value'. Primarily used for data merging. |
| 15 | `EXT_CHILD_REFERENCE_ID` | DOUBLE | NOT NULL |  | The id used to cross reference external child information to internal bill items during charging/pricing. For example, this contains the catalog_cd for order catalog items, or the task_assay_cd for discrete task assays, or the task_id for tasks. |
| 16 | `EXT_DESCRIPTION` | VARCHAR(200) |  |  | The description that will be used to define the bill item. |
| 17 | `EXT_OWNER_CD` | DOUBLE | NOT NULL |  | Code that indicates from what entry in codeset 106 this bill item was contributed. 106 entry examples include General Lab, Radiology, etc. |
| 18 | `EXT_PARENT_CONTRIBUTOR_CD` | DOUBLE | NOT NULL |  | Code that makes the parent reference id unique (in the case of multiple parent reference id sources) |
| 19 | `EXT_PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | Indicates whether the contributor for the parent was another bill item as in the case of specific as indicated by 'bill_item', or if it was an external contributor as indicated by 'code_value'. This is blank for default children. |
| 20 | `EXT_PARENT_REFERENCE_ID` | DOUBLE | NOT NULL |  | The id used to cross reference external parent information to internal bill items during charging/pricing. |
| 21 | `EXT_SHORT_DESC` | VARCHAR(50) |  |  | The short description sent from the contributor. |
| 22 | `EXT_SUB_OWNER_CD` | DOUBLE | NOT NULL |  | Code that indicates from what entry in codeset 5801 this bill item was contributed. 5801 entry examples include Toxicology, Immunology, etc. |
| 23 | `LATE_CHRG_EXCL_IND` | DOUBLE |  |  | Allows the user to designate that a bill item should always be excluded from Profit's late charge processing logic. |
| 24 | `LOGICAL_DOMAIN_ENABLED_IND` | DOUBLE | NOT NULL |  | The indicator for logical domain is enabled or not. |
| 25 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the logical domain to which this bill item is related. |
| 26 | `MISC_IND` | DOUBLE |  |  | This field is used by CSBatchChargeEntry to determine if it needs to prompt for price, description, etc. |
| 27 | `NUM_HITS` | DOUBLE |  |  | This field is essentially a counter that keeps track of the number of times this particular bill item is hit by the server. |
| 28 | `PARENT_QUAL_CD` | DOUBLE | NOT NULL |  | Indicates if the bill item is a parent. Should not have the "cd" extension. |
| 29 | `PARENT_QUAL_IND` | DOUBLE |  |  | Indicates if the bill item is a parent. |
| 30 | `PHYSICIAN_QUAL_CD` | DOUBLE | NOT NULL |  | not used |
| 31 | `STATS_ONLY_IND` | DOUBLE |  |  | This field indicates that a charge generated for this item will not be interfaced. It is captured for statistical purposes only. |
| 32 | `TAX_IND` | DOUBLE |  |  | Tax indicator |
| 33 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 34 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 35 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 36 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 37 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 38 | `WORKLOAD_ONLY_IND` | DOUBLE |  |  | Determines whether this bill item is for workload use only. It is used to filter bill items from the Pricing Tool when not in workload mode. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (17)

| From table | Column |
|------------|--------|
| [BH_GROUP_DOC](BH_GROUP_DOC.md) | `PROPOSED_BILL_ITEM_ID` |
| [BH_GROUP_DOC_PATIENT_CS](BH_GROUP_DOC_PATIENT_CS.md) | `BILL_ITEM_ID` |
| [BILL_ITEM_MODIFIER](BILL_ITEM_MODIFIER.md) | `BILL_ITEM_ID` |
| [BILL_ITEM_MODIFIER_HIST](BILL_ITEM_MODIFIER_HIST.md) | `BILL_ITEM_ID` |
| [BT_COND_CRIT_GRP_RELTN](BT_COND_CRIT_GRP_RELTN.md) | `BILL_ITEM_ID` |
| [CHARGE](CHARGE.md) | `BILL_ITEM_ID` |
| [CHARGE](CHARGE.md) | `DEF_BILL_ITEM_ID` |
| [CHARGE_BATCH_DETAIL](CHARGE_BATCH_DETAIL.md) | `BILL_ITEM_ID` |
| [GL_TRANS_QUALIFIER](GL_TRANS_QUALIFIER.md) | `BILL_ITEM_ID` |
| [PFT_BILL_ITEM_COND_CRIT_RELTN](PFT_BILL_ITEM_COND_CRIT_RELTN.md) | `BILL_ITEM_ID` |
| [PFT_REVENUE_SUMMARY](PFT_REVENUE_SUMMARY.md) | `BILL_ITEM_ID` |
| [PRICE_SCHED_ITEMS](PRICE_SCHED_ITEMS.md) | `BILL_ITEM_ID` |
| [PRICE_SCHED_ITEMS_HIST](PRICE_SCHED_ITEMS_HIST.md) | `BILL_ITEM_ID` |
| [UM_CHARGE_EVENT_ST](UM_CHARGE_EVENT_ST.md) | `BILL_ITEM_ID` |
| [UM_CHARGE_EVENT_ST](UM_CHARGE_EVENT_ST.md) | `PARENT_BILL_ITEM_ID` |
| [VISITCODING_BILLITEM](VISITCODING_BILLITEM.md) | `BILL_ITEM_ID` |
| [WORKLOAD](WORKLOAD.md) | `BILL_ITEM_ID` |

