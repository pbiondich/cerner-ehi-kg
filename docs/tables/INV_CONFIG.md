# INV_CONFIG

> Used for Custom Client Invoice

**Description:** INV CONFIG  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADDTL_SORT2_CD` | DOUBLE | NOT NULL |  | The purpose of this field is to store the second additional sort field when defining the format of a client invoice. This field acts similar to the addtl_sort_cd field |
| 6 | `ADDTL_SORT_CD` | DOUBLE | NOT NULL |  | From Inv_Sort code set |
| 7 | `ALIAS_OPTION_CD` | DOUBLE | NOT NULL |  | From Inv_Alias code set |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `DEFAULT_IND` | DOUBLE | NOT NULL |  | If a row cannot be found using the primary search criteria, the system will look for the row marked with a default_ind of 1. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `GROUP_SORT_CD` | DOUBLE | NOT NULL |  | From Inv_Sort code set |
| 12 | `INV_CONFIG_ID` | DOUBLE | NOT NULL |  | Unique identifier |
| 13 | `PATIENT_MASK_IND` | DOUBLE | NOT NULL |  | The purpose of this field is to store the value used to determine if the patient identifier is being masked from the client invoice. |
| 14 | `PRIMARY_SORT_FLAG` | DOUBLE | NOT NULL |  | The purpose of this field is to store the value used to determine what action should take place after a primary sort value changes. |
| 15 | `ROLL_CHARGES_TO_PARENT_IND` | DOUBLE |  |  | Defines whether or not client invoices will roll up child charges into their parent charges. |
| 16 | `SUMMARY_OPTION_CD` | DOUBLE | NOT NULL |  | From Inv_Summary code set |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

