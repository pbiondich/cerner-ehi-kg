# RAD_TECH_CMT_DATA_HIST

> The Rad_Tech_Cmt_Data_Hist table stores historical technical comment data for a given order.

**Description:** Radiology Tech Comment History Data  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHARTABLE_IND` | DOUBLE |  |  | The chartable_ind indicates if this field was marked as chartable at the time the data was saved |
| 2 | `DATA_CHOICE_IND` | DOUBLE |  |  | The data_choice_ind indicates if a single or multi choice field should be selected |
| 3 | `DATA_DT_TM` | DATETIME |  |  | The Data_Date field stores date data for a field that is a date type |
| 4 | `DATA_NBR` | DOUBLE |  |  | The data_nbr field stores numeric data for a field that is a numerical type. |
| 5 | `DATA_TEXT` | VARCHAR(255) |  |  | The data_text field stores text data for a field that is a textual type. |
| 6 | `FIELD_ID` | DOUBLE | NOT NULL | FK→ | The Field_Id is a foreign key to the Rad_Tech_Field table. It is used to identify a Field. |
| 7 | `MAX_NBR` | DOUBLE |  |  | The max_nbr field holds a maximum numerical value that was set for this field at the time the data was saved. The max_nbr only applies to fields that are a number type |
| 8 | `MIN_NBR` | DOUBLE |  |  | The min_nbr field holds a minimum numerical value that was set for this field at the time the data was saved. This min_nbr only applies to fields that are a number type |
| 9 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The Order_Id is a foreign key to the Orders table. It is used to uniquely identify an order. |
| 10 | `PARENT_FIELD_ID` | DOUBLE | NOT NULL | FK→ | The Parent_Field_Id is a foreign key to the Rad_Tech_Field table. It is used to identify a parent field for the row. |
| 11 | `PRSNL_UPDT_DT_TM` | DATETIME |  |  | The Prsnl_Updt_Dt_Tm identifies the date and time a personnel updated a particular field |
| 12 | `PRSNL_UPDT_ID` | DOUBLE | NOT NULL | FK→ | The Prsnl_Updt_Id identifies the personnel that updated a particular field. |
| 13 | `REQUIRED_IND` | DOUBLE |  |  | The required_ind indicates if this field was marked as required at the time the data was saved |
| 14 | `SEQUENCE` | DOUBLE | NOT NULL |  | The required_ind indicates if this field was marked as required at the time the data was saved |
| 15 | `SERIES_NBR` | DOUBLE | NOT NULL |  | The series_nbr identifies the order in which field data has changed for a given order. |
| 16 | `TECH_DATA_HIST_ID` | DOUBLE | NOT NULL |  | The Tech_Data_Hist_Id uniquely identifies a row in the Rad_Tech_Cmt_Data_Hist table. It serves no other purpose other than to uniquely identify the row |
| 17 | `TECH_DATA_ID` | DOUBLE | NOT NULL | FK→ | It is used to identify a specific tech comment field with in an order that has been changed. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FIELD_ID` | [RAD_TECH_FIELD](RAD_TECH_FIELD.md) | `FIELD_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PARENT_FIELD_ID` | [RAD_TECH_FIELD](RAD_TECH_FIELD.md) | `FIELD_ID` |
| `PRSNL_UPDT_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `TECH_DATA_ID` | [RAD_TECH_CMT_DATA](RAD_TECH_CMT_DATA.md) | `TECH_DATA_ID` |

