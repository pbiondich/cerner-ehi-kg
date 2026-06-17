# MODIFY_OPTION_TESTING

> This table contains the attributes that will be applied to the new product created for a particularmodification option.

**Description:** Modify Option Testing  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CALC_EXP_DRAWN_IND` | DOUBLE |  |  | This column is not yet used within the Modify Products application. The planned use of this indicator is for a particular modification option, it will determine whether the expiration date and time should be calculated from the drawn date and time of the blood product. A value of 1 indicates that the drawn date/time should be used. A value of 0 indicates that the modified date/time should be used instead. Currently, Modify Products always uses the modified date/time to calculate expiration. |
| 6 | `DEFAULT_EXP_DAYS` | DOUBLE |  |  | The number of days that should be used to calculate the new product's expiration date/time. This number of days will be added to the modified date/time to calculate the new product's expiration date/time. This number may be zero if the user wants to use hours (Default_Exp_Hrs) instead to calculate the new product's expiration date/time. |
| 7 | `DEFAULT_EXP_HRS` | DOUBLE |  |  | The number of hours that should be used to calculate the new product's expiration date/time. This number of hours will be added to the modified date/time to calculate the new product's expiration date/time. This number may be zero if the user wants to use days (Default_Exp_Days) instead to calculate the new product's expiration date/time. |
| 8 | `MAX_PREP_HRS` | DOUBLE |  |  | This column is not yet used within the Modify Products application. Its planned use is for a number of hours to be used to validate that the original product is still valid for being used in this particular modification option. If the maximum number of hours has passed in which to prepare the new product, it should not be allowed. It will be measured from the drawn date/time of the original product. Example: Fresh Frozen Plasma cannot be created more than 8 hours after the unit was drawn. |
| 9 | `MODIFY_OPTION_TST_ID` | DOUBLE | NOT NULL |  | This is a system-generated number that uniquely identifies a row on this table. |
| 10 | `NEW_PRODUCT_CD` | DOUBLE | NOT NULL | FK→ | The code value that represents the new product to be created during this particular modification option (ex. "Red Cells Washed"). The new product may be the same as the original product, in the case of attributes being applied to a product. |
| 11 | `OPTION_ID` | DOUBLE | NOT NULL | FK→ | The number in this column corresponds to a row on the Modify_Option table, which associates the modification option to the testing defined on this table for it. |
| 12 | `SPECIAL_TESTING_CD` | DOUBLE | NOT NULL |  | A code value that represents the special testing which should be applied to the new product created for this particular modification option. This is used to apply attributes to the new product, such as "Irradiated", "Washed", "CMV Negative" etc. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NEW_PRODUCT_CD` | [PRODUCT_INDEX](PRODUCT_INDEX.md) | `PRODUCT_CD` |
| `OPTION_ID` | [MODIFY_OPTION](MODIFY_OPTION.md) | `OPTION_ID` |

