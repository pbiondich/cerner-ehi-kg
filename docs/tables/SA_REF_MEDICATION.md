# SA_REF_MEDICATION

> Contains records that define all of the medication products that can be used in the anesthesia applications. Size - Based on the # of medications they want to define. Estimate 200 rows.

**Description:** SA Reference - Medication  
**Table type:** REFERENCE  
**Primary key:** `SA_REF_MEDICATION_ID`  
**Columns:** 13  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | The item that identifies the medication item |
| 6 | `MED_PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | The id that identifies the actual pharmacy product item FK from MED_PRODUCT |
| 7 | `REF_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of reference this item is built for (I.e Anesthesia (0), CVNet (1) |
| 8 | `SA_REF_MEDICATION_ID` | DOUBLE | NOT NULL | PK | Unique value to the medication record |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_MASTER](ITEM_MASTER.md) | `ITEM_ID` |
| `MED_PRODUCT_ID` | [MED_PRODUCT](MED_PRODUCT.md) | `MED_PRODUCT_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [SA_MEDICATION](SA_MEDICATION.md) | `SA_REF_MEDICATION_ID` |
| [SA_REF_CAT_MEDICATION](SA_REF_CAT_MEDICATION.md) | `SA_REF_MEDICATION_ID` |
| [SA_REF_EXCLUDE_MEDICATION](SA_REF_EXCLUDE_MEDICATION.md) | `SA_REF_MEDICATION_ID` |
| [SA_REF_MED_PREFERENCE](SA_REF_MED_PREFERENCE.md) | `SA_REF_MEDICATION_ID` |
| [SA_REF_REQUIRED_MEDICATION](SA_REF_REQUIRED_MEDICATION.md) | `SA_REF_MEDICATION_ID` |

