# WORKLIST_REF

> Stores the definition of worklist reference information for a worklist.

**Description:** Worklist Reference  
**Table type:** REFERENCE  
**Primary key:** `WORKLIST_REF_ID`  
**Columns:** 79  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCN_SEQ_IND` | DOUBLE | NOT NULL |  | Indicates whether the worklist is built in accession mode. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `AGE_IND` | DOUBLE | NOT NULL |  | Indicates whether to include the age on the printed worklist. |
| 7 | `AUTOMATIC_MAX_ACCN_CNT` | DOUBLE | NOT NULL |  | Defines the maximum number of accessions (i.e. specimen accessions and QC accessions) that can qualify for a given automatic worklist. This column only applies to automatic worklists of type counted. |
| 8 | `AUTOMATIC_WORKLIST_IND` | DOUBLE | NOT NULL |  | Indicates whether the worklist is defined as an automatic worklist. |
| 9 | `AUTOMATIC_WORKLIST_TYPE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the type of automatic worklist (e.g. counted, timed, etc.) |
| 10 | `AUTO_ASSIGN_IND` | DOUBLE | NOT NULL |  | Indicates whether the worklist id will automatically be assigned on the front end application or not. |
| 11 | `BACK_FRONT_FLAG` | DOUBLE | NOT NULL |  | Indicates the fill direction,1 back to front2 front to back |
| 12 | `BLANK_LINES` | DOUBLE |  |  | Defines the number of blank lines to add to the end of worklist for extra accessions that may arrive after the original worklist is printed. |
| 13 | `CLIENT_ALIAS_IND` | DOUBLE | NOT NULL |  | Indicates whether to include the Client Alias for the org that owns the paitient encounter on the printed worklist. |
| 14 | `COLLECT_DT_TM_IND` | DOUBLE | NOT NULL |  | Indicates whether to include the collected date and time on the printed worklist. |
| 15 | `COL_ALPHA_IND` | DOUBLE | NOT NULL |  | Contains the column alpha indicator on the template. |
| 16 | `COPIES` | DOUBLE |  |  | Defines the number of copies to be printed when a worklist is requested. |
| 17 | `CROSS_RESOURCE_IND` | DOUBLE |  |  | Indicates whether qualifying orders for a worklist can cross service resources. A value of 0 does not look across service resources when finding an order. A value of 1 does look across service resources when finding an order. |
| 18 | `CUMULATIVE_IND` | DOUBLE |  |  | Indicates whether a new worklist will show cumulative orders. A value of 0 indicates the orders selected will be all orders not previously placed on a worklist. A value of 1 indicates the orders selected will be all orders not yet completed. |
| 19 | `CUST_DOWNLOAD_SCRIPT_CD` | DOUBLE | NOT NULL |  | The code value corresponding to a custom download script for this worklist. |
| 20 | `DISPLAY` | VARCHAR(20) |  |  | Character description for the worklist. |
| 21 | `DISPLAY_KEY` | VARCHAR(20) |  |  | Uppercase and no spaces character value for display which is used to check and see if the display value entered for a name is new or not. |
| 22 | `DISPLAY_KEY_A_NLS` | VARCHAR(80) |  |  | DISPLAY_KEY_A_NLS column |
| 23 | `DISPLAY_KEY_NLS` | VARCHAR(42) | NOT NULL |  | Stores corresponding non-English character set values for the display_key column. |
| 24 | `FACILITY_IND` | DOUBLE |  |  | Indicates the printing of the facility associated with the patient's location on a worklist report. A value of 0 indicates the facility associated with the patient's location should not be printed on the worklist. A value of 1 indicates that the facility associated with the patient's location should be printed on the worklist. |
| 25 | `FILE_DEF_CD` | DOUBLE | NOT NULL |  | The code value corresponding to the manual download template for this worklist. |
| 26 | `FILL_FIRST_FLAG` | DOUBLE | NOT NULL |  | Indicates whether to fill rows first or columns first.1 - Row2 - Column |
| 27 | `FILTER_QC_ASSAYS_IND` | DOUBLE | NOT NULL |  | Indicates whether the QC assays will be filtered on the worksheet and in Accession Result Entry. A value of 0 indicates that the QC assays will not be filtered. A value of 1 indicates that the QC assays will be filtered. |
| 28 | `FIN_IND` | DOUBLE | NOT NULL |  | Indicates whether to include the financial number on the printed worklist. |
| 29 | `INCLUDE_FLAG` | DOUBLE |  |  | Defines whether or not to include Quality Control on the worklist. |
| 30 | `INSTR_IDENT_FLAG` | DOUBLE |  |  | Defines the identifier type for the worklist. (Currently not implemented) |
| 31 | `INTERP_TEXT_IND` | DOUBLE | NOT NULL |  | Indicates whether to include the Interpretive Text associated with an Alpha Text Interp Result when printing a worksheet. |
| 32 | `IN_LAB_IND` | DOUBLE |  |  | Indicates whether only in lab orders should qualify for a worklist report. A value of 0 indicates include all orders not completed or cancelled on the worklist. A value of 1 indicates include only the orders that are currently in lab. |
| 33 | `LANDSCAPE_IND` | DOUBLE |  |  | Indicates the page orientation of a printed worklist report. A value of 0 indicates the worklist report should print with portrait orientation on the page. A value of 1 indicates that the worklist report should print with landscape orientation on the page. |
| 34 | `LEFT_RIGHT_FLAG` | DOUBLE | NOT NULL |  | Indicates the fill direction:1 - left to right2 - right to left |
| 35 | `LOOK_AHEAD_HOURS` | DOUBLE |  |  | Defines the number of hours to look forward when selecting the orders to place on a worklist. Allows future orders to be placed on the worklist. |
| 36 | `MANUAL_DOWNLOAD_IND` | DOUBLE | NOT NULL |  | Indicates whether manual download of the worklist will be allowed. |
| 37 | `MAX_COLS_CNT` | DOUBLE | NOT NULL |  | Maximun number of columns on the template. |
| 38 | `MAX_ROWS_CNT` | DOUBLE | NOT NULL |  | Maximun number of rows on the template. |
| 39 | `MRN_IND` | DOUBLE | NOT NULL |  | Indicates whether to include the medical record number on the printed worklist. |
| 40 | `NEXT_SEQ_NUMBER` | DOUBLE | NOT NULL |  | Indicates the next sequence number to use for auto-assigning worklist aliases on the worklist table |
| 41 | `NUM_SEQ_END` | DOUBLE |  |  | Defines the ending sequence number for the identifier. (Currently not implemented) |
| 42 | `NUM_SEQ_START` | DOUBLE |  |  | Defines the beginning sequence number for the identifier. (Currently not implemented) |
| 43 | `NURSE_UNIT_IND` | DOUBLE |  |  | Indicates the printing of the nurse unit associated with the patient's location on a worklist report. A value of 0 indicates the nurse unit associated with the patient's location should not be printed on the worklist. A value of 1 indicates that the nurse unit associated with the patient's location should be printed on the worklist. |
| 44 | `ORDERING_PHYSICIAN_IND` | DOUBLE | NOT NULL |  | Indicates whether to include the ordering physician on the printed worklist. |
| 45 | `ORDER_COMMENTS_IND` | DOUBLE |  |  | Indicates the printing of the order comments and footnotes on a worklist report. A value of 0 indicates that order comments and footnotes should not print on the worklist report. A value of 1 indicates that order comments and footnotes should print on the worklist report. |
| 46 | `ORDER_STATUS_IND` | DOUBLE |  |  | Indicates the printing of the department order status on a worklist report. A value of 0 indicates that department order status should not print on the worklist report. A value of 1 indicates that department order status should print on the worklist report. |
| 47 | `OUTPUT_DEST_CD` | DOUBLE | NOT NULL |  | Indicates which printer will be used for this worklist. |
| 48 | `PARENT_IND` | DOUBLE |  |  | Defines whether the worklist reference row is a worklist print group or a worklist template definition. A value of 0 indicates the worklist reference row is a worklist template. A value of 1 indicates the worklist reference row is a worklist print group. |
| 49 | `PERSON_COMMENTS_IND` | DOUBLE |  |  | Indicates the printing of person comments and encounter comments and footnotes on a worklist report. A value of 0 indicates that person and encounter comments and footnotes should not print on the worklist report. A value of 1 indicates that person and encounter comments and footnotes should print on the worklist report. |
| 50 | `POSITIONS_PER_SPECIMEN_NBR` | DOUBLE | NOT NULL |  | Number of positions on the template for each specimen. |
| 51 | `PREVIOUS_RESULT_IND` | DOUBLE |  |  | Indicates the printing of previous result values on a worksheet report. A value of 0 indicates to not include previous results. A value of 1 indicates include previous results. |
| 52 | `PRINTER` | VARCHAR(20) |  |  | Defines the printer where the worklist will be printed. |
| 53 | `PRINT_SEQ_LEFT_IND` | DOUBLE | NOT NULL |  | Indicates whether the printed worklist should display the sequence in a new column on the left. |
| 54 | `PRIORITY_IND` | DOUBLE |  |  | Indicates the priorities to be included on a worklist report. A value of 0 indicates all priorities are selected. A value of 1 indicates only specific priorities should be included. |
| 55 | `PROCEDURE_INC_FLAG` | DOUBLE |  |  | Defines what procedures to include on the worklist. |
| 56 | `QC_RANGES_IND` | DOUBLE | NOT NULL |  | Indicates whether the expected range for a QC assay will print on the worksheet. A value of 0 indicates that the expected range for a QC assay will not print on the worksheet. A value of 1 indecates that the expected range for a QC assay will print on the worksheet. |
| 57 | `RACE_IND` | DOUBLE | NOT NULL |  | Indicates whether to include the race on the printed worklist. |
| 58 | `REPORTING_PRIORITY_IND` | DOUBLE |  |  | Indicates whether the reporting priority for a given order should print on a worklist report. A value of 0 indicates that an order's reporting priority should not print on the worklist report. A value of 1 indicates that an order's reporting priority should print on the worklist report. |
| 59 | `REPORT_FORMAT_IND` | DOUBLE |  |  | Indicates whether worklist orders or worksheet discrete task assays should print vertically or horizontally across the page. A value of 0 indicates the worklist should be printed vertically. A value of 1 indicates the worklist should be printed horizontally. |
| 60 | `REPORT_PRIORITY_IND` | DOUBLE | NOT NULL |  | Indicates whether to include the reporting priority on the printed worklist. |
| 61 | `RESULT_COMMENTS_IND` | DOUBLE |  |  | Indicates whether result comments and footnotes should print on a worksheet report. A value of 0 indicates that result comments and footnotes should not print on the worksheet report. A value of 1 indicates that result comments and footnotes should print on the worksheet report. |
| 62 | `RESULT_SPACE_IND` | DOUBLE |  |  | Indicates whether underlines should print so that results can be manually entered on the printed report. Including spaces for results changes the worklist into a worksheet. A value of 0 indicates do not include a result space on the worklist. A value of 1 indicates include a result space on the worklist. |
| 63 | `ROOM_BED_IND` | DOUBLE | NOT NULL |  | Indicates whether to include the room and bed on the printed worklist. |
| 64 | `ROW_ALPHA_IND` | DOUBLE | NOT NULL |  | Row alpha indicator on the template. |
| 65 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the service resource (instrument, bench, sub-section) to be included on the worklist. |
| 66 | `SERV_RES_SORT_IND` | DOUBLE | NOT NULL |  | Controls whether to sort the assays printed on the worklist by service resource or by catalog_cd. 0 = catalog_cd, 1 - service_resource. |
| 67 | `SEX_IND` | DOUBLE | NOT NULL |  | Indicates whether to include the sex on the printed worklist. |
| 68 | `SPACING_IND` | DOUBLE |  |  | Indicates the line spacing on the printed worklist report. A value of 0 indicates a single spaced worklist. A value of 1 indicates a double spaced worklist. |
| 69 | `SPECIMEN_TYPE_IND` | DOUBLE | NOT NULL |  | Indicates whether to include the specimen type on the printed worklist. |
| 70 | `TEMPLATE_IND` | DOUBLE | NOT NULL |  | Indicates whether this worklist will employ a template. |
| 71 | `TEXT_FREETEXT_IND` | DOUBLE | NOT NULL |  | Indicates whether to include the text or free textresults. |
| 72 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 73 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 74 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 75 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 76 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 77 | `VISIT_REASON_IND` | DOUBLE |  |  | Indicates the printing of the patient's reason for visit on the worklist report. A value of 0 indicates that the patient's reason for visit should not print on the worklist report. A value of 1 indicates that a patient's reason for visit should print on the worklist report. |
| 78 | `WORKLIST_REF_ID` | DOUBLE | NOT NULL | PK | A unique internal system assigned number that identifies a specific worklist reference template. |
| 79 | `ZIG_ZAG_IND` | DOUBLE | NOT NULL |  | Indicates whether to fill the template in a zigzag orientation. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [WORKLIST_REF_POS](WORKLIST_REF_POS.md) | `WORKLIST_REF_ID` |
| [WORKLIST_REF_PRIORITY](WORKLIST_REF_PRIORITY.md) | `WORKLIST_REF_ID` |

