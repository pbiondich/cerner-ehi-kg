# BILL_TEMPL

> Bill Template

**Description:** Stores the information related to a bill template.  
**Table type:** REFERENCE  
**Primary key:** `BILL_TEMPL_ID`  
**Columns:** 25  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BASE_TEMPL_ID` | DOUBLE | NOT NULL | FK→ | Bill Template Id of the base template from which a particular bill template was created. This is a circular reference to itself. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `BILL_TEMPL_DESC` | VARCHAR(250) |  |  | Description of the bill template. |
| 8 | `BILL_TEMPL_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 9 | `BILL_TEMPL_NAME` | VARCHAR(250) |  |  | Name of the bill template |
| 10 | `BILL_TEMPL_NAME_KEY` | VARCHAR(250) |  |  | The name of the bill template. This the bill template name in all capitols without punctuation. This will be used for indexing and searching the bill templates by name. |
| 11 | `BILL_TYPE_CD` | DOUBLE | NOT NULL |  | Code value associated to the type of bill. |
| 12 | `DETAIL_LINE_ITEM_NBR` | DOUBLE |  |  | Number of detail line item fields available on bill template. |
| 13 | `DISP_OFFSET_IND` | DOUBLE |  |  | Indicates if the offset transactions (because of adjustments, payments etc.) should be displayed on the bill. |
| 14 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 15 | `FORMAT_BILL_TYPE_CD` | DOUBLE | NOT NULL |  | Stores a code value for the secondary formatting bill type of the template object. The bill_templ has a bill_type and so does the fields. They may be different values. This table will store the default. |
| 16 | `MEDIA_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | Code value associated to the bill submission media subtype. |
| 17 | `MEDIA_TYPE_CD` | DOUBLE | NOT NULL |  | Code value associated to the bill submission media. |
| 18 | `OBJECT_NAME` | VARCHAR(30) |  |  | Name of the template generated object in the object library that corresponds to this bill template |
| 19 | `PRINT_OBJECT_NAME` | VARCHAR(30) |  |  | Name of the template generated print object in the object library that corresponds to this bill template |
| 20 | `TOTAL_UNITS_IND` | DOUBLE | NOT NULL |  | Indicates whether the client has chosen to display total units on the total line of the UB 1450. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BASE_TEMPL_ID` | [BILL_TEMPL](BILL_TEMPL.md) | `BILL_TEMPL_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [BILL_REC](BILL_REC.md) | `BILL_TEMPL_ID` |
| [BILL_TEMPL](BILL_TEMPL.md) | `BASE_TEMPL_ID` |
| [BT_FIELD_RELTN](BT_FIELD_RELTN.md) | `BILL_TEMPL_ID` |
| [BT_SELECTION](BT_SELECTION.md) | `BILL_TEMPL_ID` |
| [PFT_CHARGE_BO_RELTN](PFT_CHARGE_BO_RELTN.md) | `BILL_TEMPL_ID` |

