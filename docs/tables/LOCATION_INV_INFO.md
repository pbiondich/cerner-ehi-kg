# LOCATION_INV_INFO

> Location information specific to a location.

**Description:** Location Inventory Information  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 48

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALTERNATE_FILL_LOC_DISP_IND` | DOUBLE | NOT NULL |  | Indicates if the alternate fill locations should be displayed. |
| 2 | `ALTERNATE_VENDOR_DISP_IND` | DOUBLE | NOT NULL |  | Indicates if the alternate vendor information should be displayed. |
| 3 | `AUTO_DISTRIBUTE_IND` | DOUBLE |  |  | This indicator will be used to determine if the location is defined as auto distribute. |
| 4 | `AUTO_SELECT_LOT_IND` | DOUBLE | NOT NULL |  | Indicates if the user needs to select the lot for transfer manually or if the system will select the lot automatically. 0- manual, 1- auto |
| 5 | `BACKORDER_IND` | DOUBLE |  |  | Backorder_ind = 1 then backorders are supported at the location. Backorder_ind = 0 then the location is defined as fill/kill and quantities that are not filled will be cancelled. |
| 6 | `BACKORDER_PRINTER` | VARCHAR(40) |  |  | This attribute will be used to store the printer the backorder report will be sent too. |
| 7 | `CHK_AVAILABLE_IND` | DOUBLE |  |  | Determines whether or not Pharmnet performs inventory availability checks prior to a dispense. |
| 8 | `COST_CENTER_CD` | DOUBLE | NOT NULL |  | Cost center code value |
| 9 | `COST_FLAG` | DOUBLE | NOT NULL |  | This flag indicates whether the average cost is calculated when the quantity on hand falls below zero. |
| 10 | `COST_TYPE_CD` | DOUBLE | NOT NULL |  | Obsolete |
| 11 | `CREATE_PHYS_COUNT_TRANS_IND` | DOUBLE | NOT NULL |  | This preference indicates whether should be created. |
| 12 | `DELIVERY_TICKET_PRINTER` | VARCHAR(40) |  |  | The printer on which to print the Delivery Ticket report. |
| 13 | `FILTER_CC_SA_IND` | DOUBLE | NOT NULL |  | Indicates if the facility and all of the locations under that facility will filter cost center and sub account based on chart of accounts. |
| 14 | `FUNDING_SOURCE_CD` | DOUBLE | NOT NULL |  | Stores the relationship between the location and the vaccine provider (funding source) for a vaccine stored at the location. |
| 15 | `ITEM_FILTER_BY_LOCATION_IND` | DOUBLE | NOT NULL |  | Indicates if the item should be filtered off, if it is not present in the location. |
| 16 | `ITEM_LOCATION_TEMPLATE_TXT` | LONGTEXT |  |  | Stores the default values of item location properties in JSON format. These values would be defaulted while adding any item to the respective location. |
| 17 | `ITEM_ORG_COST_IND` | DOUBLE | NOT NULL |  | This preference indicates whether the Organization supports Org level unit cost or not. |
| 18 | `ITEM_ORG_RELTN_IND` | DOUBLE | NOT NULL |  | Indicates if this facility's organization allows items to be related to organizations. |
| 19 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | Primary Key |
| 20 | `LOCK_REQ_UOM_FLAG` | DOUBLE | NOT NULL |  | Locks the requesting unit of measure control in mmRequisition application. |
| 21 | `LOC_DISPLAY_FLAG` | DOUBLE | NOT NULL |  | This flag determines the prefix to location display. 1 = Company/Location, 2 = Company/Cost Center/Location (this is the default), 3=Cost Center/Location, 4=Location |
| 22 | `MOBILE_PICKING_IND` | DOUBLE |  |  | Indicator used to determine if the location support mobile picking or auto distribute. Mobile picking = 1, auto distribute = 0 |
| 23 | `NO_AUTO_FILL_FLAG` | DOUBLE | NOT NULL |  | This flag indicates whether requisitions will not be filled even if there is enough quantity on hand. |
| 24 | `OFFSET_ACCOUNT_IND` | DOUBLE | NOT NULL |  | Retrieve offsetting cost center and subaccount information from the clinical location for clinical adjustment transactions. |
| 25 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The organization associated with this location (used for the company code). |
| 26 | `ORG_DISPLAY_IND` | DOUBLE | NOT NULL |  | Indicates if the organization or building should be displayed in location boxes. |
| 27 | `PAR_CALC_PRINTER` | VARCHAR(40) |  |  | Printer where the PAR calculation report will be printed |
| 28 | `PATIENT_NAME_REQUIRED_IND` | DOUBLE | NOT NULL |  | Indicates whether the patient name is a mandatory field at this location. |
| 29 | `PICK_LIST_PRINTER` | VARCHAR(40) |  |  | The printer on which to print a Distribution Pick-List. |
| 30 | `PRINT_PT_BACKORDER_FLAG` | DOUBLE | NOT NULL |  | This flag indicates whether patient backorder section will be printed. |
| 31 | `PRINT_REQ_HDR_COMMENTS_IND` | DOUBLE |  |  | If true, the distribution report will include all requisition header comments. |
| 32 | `PRINT_REQ_LINE_COMMENTS_IND` | DOUBLE |  |  | f true, the distribution report will include all requisition line comments. |
| 33 | `REAL_TIME_REQ_OUTBOUND_IND` | DOUBLE | NOT NULL |  | Indicates if requisitions are sent outbound in real-time. 0 - not sent in real-time, 1 - requisitions are sent in real-time. |
| 34 | `REQ_PICK_LIST_PRINTER` | VARCHAR(40) |  |  | Printer used to print requisition pick list reports. |
| 35 | `SHELF_LABEL_PRINTER` | VARCHAR(40) |  |  | Printer used to print shelf labels |
| 36 | `SHIP_TO_LOCATION_CD` | DOUBLE | NOT NULL |  | The ship-to location for this location. |
| 37 | `SHOW_FILL_LOC_QOH_FLAG` | DOUBLE | NOT NULL |  | Shows fill location quantity on hand information in mmRequisition application. |
| 38 | `STOCK_OUT_PRINTER` | VARCHAR(40) |  |  | The printer on which to print a Stock-Out report. |
| 39 | `SUB_ACCOUNT_CD` | DOUBLE |  |  | The Sub Account Defined For Locations Inventory Information |
| 40 | `SYS_CALC_PAR_DAYS` | DOUBLE |  |  | Indicates how many days usage to take into account for calculating par levels |
| 41 | `SYS_CALC_PAR_FLAG` | DOUBLE | NOT NULL |  | Indicates whether or not the system is to recalculate par levels. |
| 42 | `TRANSFER_EXPIRED_LOT_IND` | DOUBLE | NOT NULL |  | Indicates if expired lots are to be transferred from one location to another. 0 = not, 1 - yes |
| 43 | `TWO_DECIMAL_PRECISION_IND` | DOUBLE | NOT NULL |  | A user selection field of which Decimal Precision (Either 2 or 4 digits after the decimal) that they want to use at their Organization. This preference would thereafter be referred/consumed in the Procurement workflows of Clinical Inventory Management solution to drive the calculation for several currency field values. By default, 4 Decimal precision preference would be the option selected. |
| 44 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 45 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 46 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 47 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 48 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

