# MED_DISPENSE

> The Med_dispense file stores all dispense related fields for a Med_def_flex.

**Description:** med_dispense  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 72

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALWAYS_DISPENSE_FROM_FLAG` | DOUBLE |  |  | always_dispense_from_flag |
| 2 | `BASE_ISSUE_FACTOR` | DOUBLE | NOT NULL |  | The smallest amount that a product can be divided by. |
| 3 | `BILLING_FACTOR_NBR` | DOUBLE | NOT NULL |  | Used to calculate a Charge Services billing amount, by applying the billing factor to the normal Charge Quantity. |
| 4 | `BILLING_UOM_CD` | DOUBLE | NOT NULL |  | Passed to Charge Services with the billing factor to identify the correct unit of measure for the Charge Services bill amount. |
| 5 | `CMS_WASTE_BILLING_UNIT_AMT` | DOUBLE | NOT NULL |  | Minimum waste quantity value(positive real number) based on which clinician documents waste charge. |
| 6 | `CMS_WASTE_BILLING_UNIT_UOM_CD` | DOUBLE | NOT NULL |  | Unit on which medication waste charges are appropriately calculated. |
| 7 | `CONTINUOUS_FILTER_IND` | DOUBLE |  |  | To continuously filter or not to continuously filter |
| 8 | `DISPENSE_FACTOR` | DOUBLE |  |  | The relationship between the dispense quantity and the base package of the primary manufacturer |
| 9 | `DISPENSE_QTY` | DOUBLE |  |  | The quantity amount of the dispensed product |
| 10 | `DIVISIBLE_IND` | DOUBLE |  |  | Defines whether this product can be split, broken, etc. to create a dose. |
| 11 | `FLEX_SORT_FLAG` | DOUBLE |  |  | used to appropriately sort the flex records |
| 12 | `FLEX_TYPE_CD` | DOUBLE | NOT NULL |  | This indicates the type of flex. |
| 13 | `FORMULARY_STATUS_CD` | DOUBLE | NOT NULL |  | Defines the acceptance of this product by the institution. Possible values are (as of 7/2006) Formulary, Investigational, Non-Formulary, TNF |
| 14 | `INFINITE_DIV_IND` | DOUBLE |  |  | The infinite_div_ind is set by the Pharmacy Inpatient Product Tool. If it's value is 1, the base_issue_factor is set to 0.001 to indicate infinite divisibility. |
| 15 | `INTERMITTENT_FILTER_IND` | DOUBLE |  |  | Indicates whether the drug should appear in the search results when filtered for intermittently administered drugs. |
| 16 | `INV_FACTOR_NBR` | DOUBLE | NOT NULL |  | Indicates the relationship of package information between the Pharmacy and Inventory systems. |
| 17 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | Points to the Medication_definition. Can't be 0. |
| 18 | `LABEL_RATIO` | DOUBLE |  |  | Indicates the number of labels per unit dispense quantity. |
| 19 | `LEGAL_STATUS_CD` | DOUBLE | NOT NULL |  | The legal status of the dispensed product. |
| 20 | `LOT_TRACKING_IND` | DOUBLE | NOT NULL |  | Indicates whether or not lot tracking should be required for this item. |
| 21 | `MAIL_ORDER_PROD_CD` | DOUBLE | NOT NULL |  | The value of the mail order type supported for the item. Consolidated Mail Order Pharmacy (CMOP) for item level. |
| 22 | `MAX_DOSE_QTY` | DOUBLE |  |  | The maximum quantity per dose for this item. |
| 23 | `MED_DISPENSE_ID` | DOUBLE | NOT NULL |  | Unique key of file. |
| 24 | `MED_FILTER_IND` | DOUBLE |  |  | Indicates whether this item is selectable when building a medication order. |
| 25 | `MED_PACKAGE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | The foreign key to the MED_PACKAGE_TYPE table. |
| 26 | `OE_FORMAT_FLAG` | DOUBLE |  |  | Preferred order format for this item |
| 27 | `OVERRIDE_CLSFCTN_CD` | DOUBLE | NOT NULL |  | The Code Value which determines the ability to override the classification that a medication is assigned to. |
| 28 | `PACKAGE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Relates to the package_type of the Med_def_flex. Must be greater than 0. |
| 29 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Unique Identifier from table names in Parent_Entity_Name Field. |
| 30 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | Name of the parent entity table that relates to this component |
| 31 | `PAT_ORDERABLE_IND` | DOUBLE |  |  | Defines whether or not the product is available for ordering at order entry |
| 32 | `PHARMACY_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the pharmacy type that the information belongs to. |
| 33 | `PKG_DISP_MORE_IND` | DOUBLE | NOT NULL |  | Indicates whether or not to dispense more than needed, when using Package Supply dispensing method. |
| 34 | `PKG_QTY_PER_PKG` | DOUBLE | NOT NULL |  | Indicates qty of the product within a single package |
| 35 | `POC_CHARGE_FLAG` | DOUBLE | NOT NULL |  | Indicates how a scanned Point of Care charge on administration event should be charged. |
| 36 | `PROD_ASSIGN_FLAG` | DOUBLE | NOT NULL |  | Indicates if the item is allowed to be automatically assigned.0 = Allow item to be automatically assigned; 1 = Do NOT allow item to be automatically assigned |
| 37 | `REUSABLE_IND` | DOUBLE | NOT NULL |  | This field indicates if the product is reusable, and will function for inventory incrementing purposes when products are returned to the pharmacy. Upon return to pharmacy, this product is reusable. |
| 38 | `RX_STATION_NOTES_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier on the long text table used to return the text entered in the RX Station Comment textbox. |
| 39 | `SKIP_DISPENSE_FLAG` | DOUBLE | NOT NULL |  | Indicates whether this product supports being skipped, from dispensing, when it is part of a multi-ingredient IV/Continuous order. |
| 40 | `STRENGTH` | DOUBLE |  |  | Strength of the product per unit dispense quantity. |
| 41 | `STRENGTH_UNIT_CD` | DOUBLE | NOT NULL |  | Strength unit of the dispensed product per unit dispense quantity. |
| 42 | `TPN_BALANCE_METHOD_CD` | DOUBLE | NOT NULL |  | The method used to determine which process is used for computing the mixture of electrolyte ingredients needed to deliver the ion quantities specified. |
| 43 | `TPN_CHLORIDE_PCT` | DOUBLE |  |  | If Percent Chloride balance method is chosen, this field indicates the default percent of chloride to be added in the TPN order. Integer values greater than 0 and less than or equal to 100. |
| 44 | `TPN_DEFAULT_INGRED_ITEM_ID` | DOUBLE | NOT NULL |  | The item_id for the default fill ingredient used when balancing the TPN order. |
| 45 | `TPN_FILL_METHOD_CD` | DOUBLE | NOT NULL |  | Indicates the method used for calculating volume in a TPN order. |
| 46 | `TPN_FILTER_IND` | DOUBLE |  |  | Indicator that product is built as a TPN type product |
| 47 | `TPN_INCLUDE_IONS_FLAG` | DOUBLE |  |  | Indicates whether ions contributed by ordered products should be included in the TPN balance. |
| 48 | `TPN_OVERFILL_AMT` | DOUBLE |  |  | Amount of overfill to be added to the TPN order. |
| 49 | `TPN_OVERFILL_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of measure for the volume to be added to the TPN order. Associated with column tpn_overfill_amt. |
| 50 | `TPN_PREFERRED_CATION_CD` | DOUBLE | NOT NULL |  | Indicates which cation is preferred during the balancing of the TPN order. |
| 51 | `TPN_PRODUCT_TYPE_FLAG` | DOUBLE |  |  | This flag indicates the product type for TPN products. |
| 52 | `TPN_SCALE_FLAG` | DOUBLE |  |  | This flag indicates whether the TPN product's volume is included in the order's overfill volume. |
| 53 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 54 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 55 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 56 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 57 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 58 | `USED_AS_BASE_IND` | DOUBLE |  |  | Indicates whether this product can be ordered as a base solution. |
| 59 | `VOLUME` | DOUBLE |  |  | Volume of the product per unit dispense quantity. |
| 60 | `VOLUME_UNIT_CD` | DOUBLE | NOT NULL |  | Volume unit of the dispensed product per unit dispense quantity. |
| 61 | `WASTE_CHARGE_IND` | DOUBLE | NOT NULL |  | Tells whether waste charge is enabled at Product/Facility level. |
| 62 | `WITNESS_ADHOC_IND` | DOUBLE | NOT NULL |  | Value of 1 indicates this medication requires a witness to perform an Ad Hoc Transaction. |
| 63 | `WITNESS_ADHOC_REFILL_IND` | DOUBLE | NOT NULL |  | Indicates if this medication requires a witness when performing an ad hoc refill. |
| 64 | `WITNESS_DISPENSE_IND` | DOUBLE | NOT NULL |  | Value of 1 indicates this medication requires a witness to perform a Dispense transaction. |
| 65 | `WITNESS_EMPTY_RETURN_IND` | DOUBLE | NOT NULL |  | Indicates if this medication requires a witness when performing an Empty return. |
| 66 | `WITNESS_EXPIRE_MGMT_IND` | DOUBLE | NOT NULL |  | Indicates whether this medication requires a witness to perform expiration management. |
| 67 | `WITNESS_INV_COUNT_IND` | DOUBLE | NOT NULL |  | Indicates whether this medication requires a witness to perform an inventory count. |
| 68 | `WITNESS_OVERRIDE_IND` | DOUBLE | NOT NULL |  | Value of 1 indicates this medication requires a witness to perform an Override transaction. |
| 69 | `WITNESS_RETURN_IND` | DOUBLE | NOT NULL |  | Value of 1 indicates this medication requires a witness to perform a Return transaction. |
| 70 | `WITNESS_SCHED_TASK_IND` | DOUBLE | NOT NULL |  | Indicates if this medication requires a witness when performing a scheduled task. |
| 71 | `WITNESS_WASTE_IND` | DOUBLE | NOT NULL |  | Value of 1 indicates this medication requires a witness to perform a Waste transaction. |
| 72 | `WORKFLOW_CD` | DOUBLE | NOT NULL |  | The dispense sequence associated to the product which is used to route orders to the dispense monitor. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `MED_PACKAGE_TYPE_ID` | [MED_PACKAGE_TYPE](MED_PACKAGE_TYPE.md) | `MED_PACKAGE_TYPE_ID` |
| `PACKAGE_TYPE_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |
| `RX_STATION_NOTES_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

