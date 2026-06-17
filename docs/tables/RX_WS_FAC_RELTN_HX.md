# RX_WS_FAC_RELTN_HX

> Contains historical reference data about Worksheets at a location. A worksheet is created in the RX_WS table. When it is approved there, a row is written to this RX_WS_FAC_RELTN_HX table. A row in this table signifies that a worksheet is available for use.

**Description:** Pharmacy Worksheet Facility Relation History  
**Table type:** REFERENCE  
**Primary key:** `RX_WS_FAC_RELTN_HX_ID`  
**Columns:** 30  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `APPROVED_DT_TM` | DATETIME |  |  | Date/time the worksheet was approved for actual use. |
| 3 | `APPROVED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person who approved the worksheet for actual use. |
| 4 | `APPROVED_TZ` | DOUBLE | NOT NULL |  | Time zone associated with APPROVED_DT_TM. |
| 5 | `FAC_CD` | DOUBLE | NOT NULL | FK→ | The facility that the Pharmacy Worksheet is valid for. |
| 6 | `LABEL_FORMAT_CD` | DOUBLE | NOT NULL |  | The label associated to the Pharmacy Worksheet. |
| 7 | `LABOR_COST_AMT` | DOUBLE | NOT NULL |  | The total cost of the labor required to create the parent item. |
| 8 | `LABOR_NBR` | DOUBLE | NOT NULL |  | The amount of time that is required to create the parent item. |
| 9 | `LABOR_RATIO_IND` | DOUBLE | NOT NULL |  | Indicates whether the labor and labor costs are directly associated to the number of items created. |
| 10 | `LABOR_UNIT_CD` | DOUBLE | NOT NULL |  | The unit for the amount of time that is required to create the parent item. |
| 11 | `MAINTAIN_RATIO_IND` | DOUBLE | NOT NULL |  | Indicates whether or not the quantity created by the worksheet is directly related to the child item quantities for the parent item. |
| 12 | `MIXING_INSTR_TEXT_ID` | DOUBLE | NOT NULL |  | The mixing instructions required to create the parent item. |
| 13 | `PARENT_ITEM_ID` | DOUBLE | NOT NULL |  | The item that is created by the worksheet. |
| 14 | `PHARMACY_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the pharmacy type that the worksheet will be created for. |
| 15 | `REPORT_FORMAT_CD` | DOUBLE | NOT NULL |  | The report associated to the Pharmacy Worksheet. |
| 16 | `RX_WS_FAC_RELTN_HX_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a unique row on the RX_WS_FAC_RELTN_HX table. |
| 17 | `RX_WS_ID` | DOUBLE | NOT NULL | FK→ | Identifies the worksheet that is valid at a specific location. |
| 18 | `SHELF_LIFE_NBR` | DOUBLE | NOT NULL |  | The amount of time that the parent item is good for. (Expiration Date) |
| 19 | `SHELF_LIFE_UNIT_CD` | DOUBLE | NOT NULL |  | The unit for the amount of time that the parent item is good for. |
| 20 | `TOTAL_QTY` | DOUBLE | NOT NULL |  | Indicates the amount of the parent item that will be created by the Pharmacy Worksheet. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 26 | `WS_BEGIN_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 27 | `WS_BEGIN_EFFECTIVE_TZ` | DOUBLE | NOT NULL |  | Time zone associated with WS_BEGIN_EFFECTIVE_DT_TM. |
| 28 | `WS_CD` | DOUBLE | NOT NULL |  | The code value for the Pharmacy Worksheet. |
| 29 | `WS_END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 30 | `WS_END_EFFECTIVE_TZ` | DOUBLE | NOT NULL |  | Time zone associated with WS_END_EFFECTIVE_DT_TM. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `APPROVED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `FAC_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `RX_WS_ID` | [RX_WS](RX_WS.md) | `RX_WS_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [RX_WF_WS](RX_WF_WS.md) | `RX_WS_FAC_RELTN_HX_ID` |
| [RX_WS_FAC_ITEM_HX](RX_WS_FAC_ITEM_HX.md) | `RX_WS_FAC_RELTN_HX_ID` |

