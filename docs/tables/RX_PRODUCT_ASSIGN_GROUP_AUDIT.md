# RX_PRODUCT_ASSIGN_GROUP_AUDIT

> The table is used to log order catalog group level information when system attempts to assign pharmacy products automatically. It records input information common to all items to be product assigned within a group. For example, an order with one or more ingredients is considered a group.

**Description:** Pharmacy product assign audit table at catalog group level.  
**Table type:** ACTIVITY  
**Primary key:** `CATALOG_GROUP_ID`  
**Columns:** 15  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_GROUP_ID` | DOUBLE | NOT NULL | PK | Unique identifier. |
| 2 | `CONTINUOUS_FILTER_IND` | DOUBLE | NOT NULL |  | Match products built to be dispensed as continuous infusion. It is used to filter down the list of products qualify for auto product assign. 0: product can be dispensed as continuous infusion or not is irrelevant for the purpose of product filtering. Products do not have to be built as continuous infusion to qualify for product assign. 1: only products built as continuous infusion qualify for product assign |
| 3 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | Encounter type code (encntr_type_cd) from patient encounter. It's used to flex product defaults on the selected product. |
| 4 | `FACILITY_CD` | DOUBLE | NOT NULL |  | Facility code (loc_facility_cd) from patient encounter. It is used to filter down the list of products qualify for auto product assign. It is also used to flex product defaults on the selected product. |
| 5 | `FORM_CD` | DOUBLE | NOT NULL |  | Code value for drug form. It is used to filter down the list of products qualify for auto product assign. |
| 6 | `INTERMITTENT_FILTER_IND` | DOUBLE | NOT NULL |  | Match products built to be dispensed as intermittent. It is used to filter down the list of products qualify for auto product assign. 0: product can be dispensed as intermittent or not is irrelevant for the purpose of product filtering. Products do not have to be built as intermittent to qualify for product assign. 1: only products built as intermittent qualify for product assign |
| 7 | `MED_FILTER_IND` | DOUBLE | NOT NULL |  | Match products built to be dispensed as medications. It is used to filter down the list of products qualify for auto product assign. 0: product can be dispensed as medication or not is irrelevant for the purpose of product filtering. Products do not have to be built as medication to qualify for product assign. 1: only products built as medication qualify for product assign At least one of med_filter_ind, continuous_filter_ind and intermittent_filter_ind needs to be 1. |
| 8 | `PAT_LOCN_CD` | DOUBLE | NOT NULL |  | Patient location code (loc_nurse_unit_cd) from patient encounter. It is used to flex product defaults on the selected product. |
| 9 | `ROUTE_CD` | DOUBLE | NOT NULL |  | Code value for route of the medication. It is used to filter down the list of products qualify for auto product assign. |
| 10 | `SKIP_IV_SET_IND` | DOUBLE | NOT NULL |  | Whether or not attempt to match on IV sets. 0: do not match IV sets 1: match IV sets |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [RX_AUTO_VERIFY_AUDIT](RX_AUTO_VERIFY_AUDIT.md) | `CATALOG_GROUP_ID` |
| [RX_PRODUCT_ASSIGN_AUDIT](RX_PRODUCT_ASSIGN_AUDIT.md) | `CATALOG_GROUP_ID` |
| [RX_PRODUCT_ASSIGN_ITEM_AUDIT](RX_PRODUCT_ASSIGN_ITEM_AUDIT.md) | `CATALOG_GROUP_ID` |

