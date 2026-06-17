# MM_ROL_TEMPLATE

> Contains all of the templates created for Recommended Order List so user can load previously created template and execute the application using the template.

**Description:** MM Role Template  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 36

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLASS_NODE1_ID` | DOUBLE | NOT NULL |  | The first of up to 5 class nodes in the template used as filters for the item. |
| 2 | `CLASS_NODE2_ID` | DOUBLE | NOT NULL |  | % noded % |
| 3 | `CLASS_NODE3_ID` | DOUBLE | NOT NULL |  | % noded % |
| 4 | `CLASS_NODE4_ID` | DOUBLE | NOT NULL |  | The fourth of up to 5 class nodes in the template used as filters for the item. |
| 5 | `CLASS_NODE5_ID` | DOUBLE | NOT NULL |  | The last of up to 5 class nodes in the template used as filters for the item. |
| 6 | `COMMIT_IND` | DOUBLE |  |  | Indicator to commit internally sourced requisition. |
| 7 | `CREATE_ES_IND` | DOUBLE |  |  | Indicator to create externally sourced requisition. |
| 8 | `CREATE_IS_IND` | DOUBLE |  |  | Indicator to create internally sourced requisition. |
| 9 | `EXT_COMMIT_IND` | DOUBLE | NOT NULL |  | Commit indicator for externally-sourced requisition. |
| 10 | `FILL_LOCATION1_CD` | DOUBLE | NOT NULL |  | The first of up to 5 fill locations for the ordering location. |
| 11 | `FILL_LOCATION2_CD` | DOUBLE | NOT NULL |  | The second of up to 5 fill locations for the ordering location. |
| 12 | `FILL_LOCATION3_CD` | DOUBLE | NOT NULL |  | The third of up to 5 fill locations for the ordering location. |
| 13 | `FILL_LOCATION4_CD` | DOUBLE | NOT NULL |  | The fourth of up to 5 fill locations for the ordering location. |
| 14 | `FILL_LOCATION5_CD` | DOUBLE | NOT NULL |  | The last of up to 5 fill locations for the ordering location. |
| 15 | `FROM_DT_TM` | DATETIME |  |  | The beginning date for this period. |
| 16 | `ITEM_A_IND` | DOUBLE |  |  | Indicator to only retrieve item under 'A' classification (based on the price). |
| 17 | `ITEM_B_IND` | DOUBLE |  |  | Indicator to only retrieve item under 'B' classification (based on the price). |
| 18 | `ITEM_C_IND` | DOUBLE |  |  | Indicator to only retrieve item under 'C' classification (based on the price). |
| 19 | `ITEM_TYPE_CD` | DOUBLE | NOT NULL |  | The type of items that should be retrieved. Can be item master, equipment master, medication definition or all 3 types. |
| 20 | `ORDER_LOCATION_CD` | DOUBLE | NOT NULL |  | The location where the order was placed. |
| 21 | `OUTPUT_DIST` | VARCHAR(100) |  |  | Where the ROL report should print. |
| 22 | `RECALC_TYPE_CD` | DOUBLE | NOT NULL |  | How ROL will recalculate the reorder quantity. Can be PAR method, economic quantity method or all reorder types method. |
| 23 | `REPORT_TYPE_CD` | DOUBLE | NOT NULL |  | The coded identifier for the scheduling report type. |
| 24 | `ROOT_LOC_CD` | DOUBLE | NOT NULL |  | The inventory view for this route. |
| 25 | `TEMPLATE_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the MM_ROL_TEMPLATE table. |
| 26 | `TEMPLATE_NAME` | VARCHAR(60) |  |  | The name of the template. |
| 27 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 28 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 29 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 30 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 31 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 32 | `VENDOR1_CD` | DOUBLE | NOT NULL |  | The first of up to 5 vendors designated to fill the ordering location. |
| 33 | `VENDOR2_CD` | DOUBLE | NOT NULL |  | The second of up to 5 vendors designated to fill the ordering location. |
| 34 | `VENDOR3_CD` | DOUBLE | NOT NULL |  | The third of up to 5 vendors designated to fill the ordering location. |
| 35 | `VENDOR4_CD` | DOUBLE | NOT NULL |  | The fourth of up to 5 vendors designated to fill the ordering location. |
| 36 | `VENDOR5_CD` | DOUBLE | NOT NULL |  | The last of up to 5 vendors designated to fill the ordering location. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

