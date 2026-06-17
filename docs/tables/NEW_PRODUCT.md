# NEW_PRODUCT

> A reference of the new products defined for each type of product modification which creates new products from the original one.

**Description:** New Product  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `DEFAULT_EXP_DAYS` | DOUBLE |  |  | Defines the default expiration that should be calculated for the new product created during modification. The system will add this number of days to the modification date and time, to calculate the default expiration date and time for the new product. (The system also uses the number of hours defined in the DEFAULT_EXP_HRS column.) |
| 6 | `DEFAULT_EXP_HRS` | DOUBLE |  |  | Defines the default expiration that should be calculated for the new product created during modification. The system will add this number of hours to the modification date and time, to calculate the default expiration date and time for the new product. (The system also uses the number of days defined in the DEFAULT_EXP_DAYS column.) |
| 7 | `DEFAULT_MEASURE_IND` | DOUBLE |  |  | Defines whether or not the unit of measure of the new product should be defaulted at the time of modification. |
| 8 | `DEFAULT_UNIT_MEASURE_CD` | DOUBLE | NOT NULL |  | Represents the code value for the unit of measure that should be displayed as the default value for the new product being created during the modification transaction. This column may be blank (zero) if the user does not wish to have a default unit of measure displayed at all. |
| 9 | `DEFAULT_VOLUME` | DOUBLE |  |  | Defines the volume that should be displayed as the default value for the new product being created during the modification transaction. This column may be blank (zero) if the user does not wish to have a default volume displayed at all. |
| 10 | `DEFAULT_VOLUME_IND` | DOUBLE |  |  | Defines whether or not the volume of the new product should be defaulted at the time of modification. |
| 11 | `DFLT_ORIG_VOLUME_IND` | DOUBLE | NOT NULL |  | Indicates that the volume of the original product should be used as the default volume for the new product. |
| 12 | `MAX_PREP_HRS` | DOUBLE |  |  | Defines the validation that should occur, if any, on whether the product is too "old" to be modified. An example is creating fresh frozen plasma, which must be done within eight hours after the original product is drawn from the donor. The system will add the number of hours defined in this column to the drawn date of the product, and validate whether the modification date and time entered is less than the maximum date and time calculated. |
| 13 | `NEW_PRODUCT_CD` | DOUBLE | NOT NULL |  | The code value for the new product type to be created from the |
| 14 | `OPTION_ID` | DOUBLE | NOT NULL | FK→ | Part of the primary key of this table. An internal system-assigned number that is the sole primary key of the MODIFY_OPTION table. The value in this column corresponds to a row on the MODIFY_OPTION table, in order to link a specific modification option with the new products created for that option. |
| 15 | `QUANTITY` | DOUBLE |  |  | This column applies only to modification options for splitting the original product into multiple bags of the same product type (refer to the DIVISION_TYPE_FLAG column). The number in this column defines the number of new products that the modification process should generate from the original product entered. |
| 16 | `SPECIAL_TESTING_CD` | DOUBLE | NOT NULL |  | The code value that represents the special testing, if any, that should be added to the new product created from the modification process. This includes any product attributes, such as "Irradiated", "Washed", etc. |
| 17 | `SUB_PROD_ID_FLAG` | DOUBLE |  |  | Defines the type of sub product ID that should be assigned to each new product created during modification, in order to make each product unique for the same product number. The type of sub product number defined here will be displayed as a default on modifications with different product types created. On modifications that split the original product into multiple ones, this sub product number will be automatically assigned by the system to new products created. |
| 18 | `SYNONYM_ID` | DOUBLE | NOT NULL |  | This column represents the confirmatory test, if applicable, that should be automatically ordered on the product at the time it is modified. This confirmatory test is built in the order catalog and given a synonym, which this column represents. It is the primary key of the SYNONYM table, and is an internal system-assigned number. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OPTION_ID` | [MODIFY_OPTION](MODIFY_OPTION.md) | `OPTION_ID` |

