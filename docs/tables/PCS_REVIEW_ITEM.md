# PCS_REVIEW_ITEM

> Stores the review items that are assigned to queues used for Clinical Validation. A review item may be an order, a specific task assay or a Microbiology task.

**Description:** Stores review items for Clinical Validation.  
**Table type:** ACTIVITY  
**Primary key:** `REVIEW_ID`  
**Columns:** 25  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BB_COMPLETE_ORDER_IND` | DOUBLE | NOT NULL |  | Indicates whether the order status should be updated to complete when a blood bank order has reached final approval. This option is applicable to Blood Bank Antibody ID and Antigen ID orders that have the blood bank result entry preference set to prompt the user to determine if the order should be completed. Valid values are: 0 = Don't update order to complete on final approval, 1 = User answered yes to the complete order prompt. Update order to complete on final approval. |
| 6 | `BB_RH_PHENO_DEMOG_IND` | DOUBLE | NOT NULL |  | Indicates whether the person or product demographic Rh Phenotype should be changed. This option is applicable to Blood Bank Rh Phenotype Order when Result Entry prompt user whether to update demographic Rh Phenotype. Valid values are: 0 = Don't update demographic Rh Phenotype, 1 = Update demographic Rh Phenotype |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `COMPLETED_DT_TM` | DATETIME |  |  | Contains date the entire review was completed. |
| 9 | `CURRENT_USER_ID` | DOUBLE | NOT NULL |  | Contains the internal identification code that uniquely identifies personnel. This field is used to indicate if the review item is currently being reviewed essentially locking it. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `HIERARCHY_ID` | DOUBLE | NOT NULL | FK→ | Contains the internal identification code that uniquely identifies an order. This field is used to join to other tables such as ORDERS. |
| 12 | `MICRO_TASK_TYPE_CD` | DOUBLE | NOT NULL |  | This is for MICRO to indicate whether this is a preliminary, final, or amended report. |
| 13 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Contains the internal identification code that uniquely identifies an order. This field is used to join to other tables such as ORDERS. |
| 14 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Contains the internal identification code that uniquely identifies the row on the table named in parent_entity_name field. This field is used to join to other tables such as DISCRETE_TASK_ASSAY. |
| 15 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Contains table name for parent_entity_id field. Valid table names include:RESULT, ORDER, MIC_TASK_LOG |
| 16 | `PENDING_DT_TM` | DATETIME |  |  | The date/time this row went into a pending status. |
| 17 | `REVIEW_CRITERIA_ID` | DOUBLE | NOT NULL | FK→ | Contains the internal identification code that uniquely identifies review criteria. This field is used to join to other tables such as PCS_REVIEW_CRITERIA. |
| 18 | `REVIEW_ID` | DOUBLE | NOT NULL | PK | Contains the internal identification code that uniquely identifies a review item. |
| 19 | `REVIEW_STATUS_CD` | DOUBLE | NOT NULL |  | This is the status of the review item. Code set 29161. |
| 20 | `ROUTE_PREF_FLAG` | DOUBLE |  |  | Route preference of the qualifying criteria at the time the review item qualified for review. Flag values are: 0 - Micro Task; 1 = Order Level Route; 2 = All Assay Level Route; 3 = Assay Level Route |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HIERARCHY_ID` | [PCS_HIERARCHY](PCS_HIERARCHY.md) | `HIERARCHY_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `REVIEW_CRITERIA_ID` | [PCS_REVIEW_CRITERIA](PCS_REVIEW_CRITERIA.md) | `REVIEW_CRITERIA_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PCS_QUALIFYING_CRITERIA](PCS_QUALIFYING_CRITERIA.md) | `REVIEW_ID` |
| [PCS_QUEUE_ASSIGNMENT](PCS_QUEUE_ASSIGNMENT.md) | `REVIEW_ID` |

