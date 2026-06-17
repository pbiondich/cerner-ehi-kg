# RAD_FOL_UP_FIELD_VALUES

> The Rad_Fol_Up_Field_Values table contains valid values for the follow up fields used for classification.

**Description:** Rad Follow Up Field Values  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACR_CODED_FIELD` | CHAR(10) |  |  | The ACR_Coded_Field contains a code that is supplied by the American College of Radiology. This code is downloaded with the data and returned to the ACR. Certain fields are required by the ACR. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `FOLLOW_UP_FIELD_ID` | DOUBLE |  |  | The Follow_Up_Field_Id serves as a foreign key to the Rad_Fol_Up_Field table. It identifies the follow up field that this value is associated with. |
| 4 | `FOLLOW_UP_VALUE_ID` | DOUBLE | NOT NULL |  | The Follow_Up_Value_Id uniquely identifies a row in the Rad_Fol_Up_Field_Values table. It serves no other purpose other than to uniquely identify the row. |
| 5 | `MODIFY_IND` | DOUBLE |  |  | The Modify_Ind indicates if the follow up field value is modifiable or not. Certain fields and field values are required by the ACR. |
| 6 | `SEQUENCE` | DOUBLE |  |  | The Sequence indicates the order that the field values should appear in a list. |
| 7 | `SUB_FIELD_ID` | DOUBLE |  |  | The Sub_Field_Id serves as a foreign key to the Rad_Fol_Up_Field table. It identifies another field that is related to this specific value. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `VALUE_DESCRIPTION` | VARCHAR(255) |  |  | The Value_Description contains the actual textual response that can be chosen from a list. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

